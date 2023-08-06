from django.db import models
from django.db import models
from django.core.exceptions import ValidationError
from sqlalchemy import *
from sqlalchemy.orm import *
from .datasources import datasources
from .actions import ActionsManager
import urllib.parse
import json
import pgcrypto
import logging
import schedule
import time
from datetime import datetime
import logging
import traceback
import sys
import os


cached_database_metas = {}
database_engines = {}


class Database(models.Model):
    """
    This data model describes a database connection information and it
    provides functions to interact with databases.
    """
    handle = models.SlugField(
        max_length=200,
        help_text='Set a unique name for this database'
    )
    source = models.IntegerField(
        choices=datasources.touple,
        help_text='Select what kind of SQL database this is'
    )
    config = pgcrypto.EncryptedTextField(
        max_length=1000,
        help_text='Set connection information and credentials'
    )
    description = models.CharField(
        max_length=200,
        help_text='Describe what this database is all about'
    )

    def __str__(self):
        return self.handle

    def configs():
        return datasources.__list__

    def mount(self):
        """
        This function returns an instance of an SQLAlchemy database_engine of
         the database configured in the object calling the method.

        For perfomance, each time this function is called, it saves a copy of
         the engine in the database_engines dictionary so that when it's called
         again for the same database, it will first look in the dictionary and
         if it find that the engine is already saved there, it will return it

        """
        if str(self.pk) in database_engines:
            # Run garbage collector to dispose old IDLE connections
            # database_engines[str(self.pk)].dispose()
            return database_engines[str(self.pk)]
        config = json.loads(self.config)
        connectionStr = datasources.__list__[self.source]['dialect'] + '://'
        if 'dbfile' in config:
            connectionStr += '/' + config['dbfile']
        else:
            connectionStr += (
                urllib.parse.quote_plus(config['user'])
                + ":"
                + urllib.parse.quote_plus(config['password'])
                + "@"
            )
            connectionStr += config['host']
            if "port" in config:
                connectionStr += ":"
                connectionStr += str(config["port"])
            connectionStr += "/" + config["dbname"]
        database_engines[str(self.pk)] = create_engine(
            connectionStr,
            echo=False
        )
        return database_engines[str(self.pk)]

    def tables(self):
        """
        This function returns a list of all tables in the database from which
         the function is being called.
        """
        from .methods import make_query
        with self.mount().connect() as connection:
            results = []
            if self.source == datasources.SQLIGHT:
                ret = connection.execute(make_query(datasources.__list__[
                    self.source]['dialect'] + '/list_tables'))
            else:
                ret = connection.execute(make_query('list_tables'))
            for record in ret:
                results.append(record[0])
            return results

    def meta(self, schema=None, refresh=False):
        """
        This function returns an SQLAlchemy database MetaData object of the
         database from which the function is being called.

        For perfomance, each time this function is called, it saved a copy
         of the MetaData object in the cached_database_metas dictionary so
         that when it's called again for the same database, it will first
         look in the dictionary and if it found that the MetaDate is already
         saved there, it will return it directly from there.

        Parameters
        ----------
            schema (str | None): The schema name to get the MetaData for.
                Default is 'public'

            refresh (boolean): Whether to reload the MetaData from the
                server or use the cached copy instead for performance.
        """
        db = self.mount()
        metaid = '{0}.{1}'.format(self.pk, schema)
        if metaid in cached_database_metas and not refresh:
            return cached_database_metas[metaid]
        else:
            logging.debug(
                'Loading meta data for {0} schema {1}'
                .format(self, schema)
            )
            cached_database_metas[metaid] = MetaData(schema=schema)
            cached_database_metas[metaid].reflect(bind=db)
            return cached_database_metas[metaid]

    def get_table(self, table, schema=None, refresh=False):
        """
        This function returns an SQLAlchemy Table object for the table
         identified by 'table', and 'schema' (optional)

        Parameters
        ----------
            table (str): The name of the table to retrive

            schema (str | None): The schema containing the intended table.
                Default is None, which refers to the public schema.

            refresh (boolean): Whether to load the table structure from the
                database or to use the cached meta data instead
                for performance.
        """
        meta = self.meta(schema, refresh=refresh)
        if schema is not None:
            table = schema + '.' + table
        if table in meta.tables:
            return meta.tables[table]
        else:
            return None

    def clean(self):
        """
        This function is used to validate database connection information
         before saving it.
        """
        try:
            with self.mount().connect() as connection:
                None  # Just testing the connection
        except Exception as e:
            raise ValidationError(
                'Failed to connect to database: {0}'.format(e))


class StateWatcher(models.Model):
    name = models.CharField(
        help_text='Describe this state watcher or give it a name',
        max_length=200
    )
    database = models.ForeignKey(
        Database,
        on_delete=models.CASCADE,
        help_text=(
            'The database containing the state data to watch'
        )
    )
    query = models.CharField(
        help_text=(
            'SQL statment that will be used to get some state'
            + ' data that needs to be watched'
        ),
        max_length=10000
    )
    interval = models.IntegerField(
        help_text=(
            'Time interval in minutes on which the state'
            ' will be evaluated'
        )
    )
    identity = models.CharField(
        help_text=(
            '(This is required in case the query can possibly '
            'return more than one record) identity column is used'
            ' to identify which record has been removed in case'
            ' the number of record dropped to less than it used'
            ' to be in the previous interval'
        ),
        max_length=100
    )
    target = models.CharField(
        help_text=(
            'Webhook link to which notifications will be sent or'
            ' path to python function to execute'
        ),
        max_length=1000,
        choices=ActionsManager.choices()
    )
    last_state = models.CharField(max_length=1073741824, editable=False)

    scheduled_watchers = {}

    def __str__(self):
        return self.name

    def get_state(self):
        """Rerun the query to get current state
        """
        with self.database.mount().connect() as dbc:
            state = [
                dict(record)
                for record in dbc.execute(self.query).fetchall()
            ]
            return state

    def comp(self, old_state, new_state):
        """Compare new state and old state and return a
        summary of changes

        Args:
            old_state (list | None): The old state
            new_state (list): The current state

        Returns:
            dict: dictionary with zero of more of the
            following keys
                - old_dict: Containes a dict where each key is
                    an id for a record and each value is a
                    record. It contains information based on
                    the old_state provided
                - new_dict: Containes a dict where each key is
                    an id for a record and each value is a
                    record. It contains information based on
                    the new_state provided
                - added: Contains a list of records added
                - removed: Contains a list of records removed
                - modified: Contains a dict having keys being
                the identity column of records that has been
                modified and values being a dict having keys
                being name of fields that has been modified
                and values being a dict having two keys:
                    - old: The old value of the modified field
                    - new: The new value of the modified filed
        """
        if old_state is None:
            old_state = []
        id = self.identity
        old_dict = {}
        new_dict = {}
        common_ids = {}
        added = []
        removed = []
        modified = {}
        for r in old_state:
            old_dict[r[id]] = r
        for r in new_state:
            new_dict[r[id]] = r
            if r[id] not in old_dict:
                added.append(r)
            else:
                common_ids[r[id]] = True
        for r in old_state:
            if r[id] not in new_dict:
                removed.append(r)
        for i in common_ids:
            modifications = {}
            for k in old_dict[i]:
                if old_dict[i][k] != new_dict[i][k]:
                    modifications[k] = {
                        "old": old_dict[i][k],
                        "new": new_dict[i][k]
                    }
            if modifications:
                modified[i] = modifications
        results = {
            "old_dict": old_dict,
            "new_dict": new_dict
        }
        if added:
            results["added"] = added
        if removed:
            results["removed"] = removed
        if modified:
            results["modified"] = modified
        return results

    def update(self):
        """This function should be called periodically as per self.interval
        """
        try:
            new_state = self.get_state()
            old_state = \
                json.loads(self.last_state) if self.last_state else None
            diff = self.comp(old_state, new_state)
            self.last_state = json.dumps(new_state)
            self.save()
            return diff
        except Exception as exc:
            ct = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            logging.warning(
                f"{ct} StateWatcher({self}).update failed with exception: \n"
                f"{exc_type.__name__} in {fname} at line {exc_tb.tb_lineno}\n"
                f"{traceback.format_exc()}"
            )

    def refresh(self):
        self = StateWatcher.objects.get(id=self.id)
        changes = self.update()
        if changes:
            try:
                ActionsManager.actions_map[self.target](changes)
            except Exception as exc:
                ct = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                logging.warning(
                    f"{ct} StateWatcher({self}).refresh failed with "
                    f"exception: \n{exc_type.__name__} in {fname} at line"
                    f" {exc_tb.tb_lineno}\n{traceback.format_exc()}"
                )

    @classmethod
    def _update_scheduled_jobs(cls):
        added_jobs = {}
        removed_jobs = {}
        modified_jobs = {}
        for id in cls.scheduled_watchers:
            if not cls.objects.filter(id=id).exists():
                removed_jobs[id] = cls.objects.filter(id=id)[0]
            elif cls.objects.filter(id=id)[0].interval != \
                    cls.scheduled_watchers[id]["interval"]:
                modified_jobs[id] = cls.objects.filter(id=id)[0]
        for obj in cls.objects.all():
            if obj.id not in cls.scheduled_watchers:
                added_jobs[obj.id] = obj
        for id in added_jobs:
            job_obj = added_jobs[id]
            cls.scheduled_watchers[id] = {
                "job": schedule.every(
                    job_obj.interval
                ).minutes.do(job_obj.refresh),
                "interval": job_obj.interval
            }
        for id in removed_jobs:
            schedule.cancel_job(cls.scheduled_watchers[id]["job"])
            del cls.scheduled_watchers[id]
        for id in modified_jobs:
            job_obj = modified_jobs[id]
            schedule.cancel_job(cls.scheduled_watchers[id]["job"])
            cls.scheduled_watchers[id]["job"] = \
                schedule.every(job_obj.interval).minutes.do(job_obj.refresh)
            cls.scheduled_watchers[id]["interval"] = job_obj.interval
        if len(added_jobs):
            logging.info(f"{len(added_jobs)} Watchers added")
        if len(removed_jobs):
            logging.info(f"{len(removed_jobs)} Watchers removed")
        if len(modified_jobs):
            logging.info(f"{len(modified_jobs)} Watchers modified")

    @classmethod
    def start(cls):
        """Start all StateWatchers in Alert360
        """
        for sw in cls.objects.all():
            cls.scheduled_watchers[sw.id] = \
                {
                    "job": schedule.every(sw.interval).minutes.do(sw.refresh),
                    "interval": sw.interval
            }
        schedule.every(2).seconds.do(cls._update_scheduled_jobs)
        while True:
            schedule.run_pending()
            time.sleep(1)
