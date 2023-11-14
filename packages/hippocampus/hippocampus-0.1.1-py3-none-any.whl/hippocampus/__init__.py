"""
Main file
"""
import functools
import inspect
import pathlib
import datetime

import dateparser
import orjson
from pip._internal.utils.appdirs import user_cache_dir

from peewee import *
from playhouse.sqlite_ext import *

cache_dir = pathlib.Path(user_cache_dir('hippocampus'))
cache_dir.mkdir(exist_ok=True, parents=True)

db = SqliteDatabase(cache_dir / 'db.sqlite3',
                    pragmas={'journal_mode': 'wal',
                             'cache_size': -1024 * 1000})


class MemoizedCall(Model):
    fn_name = CharField()
    arguments = JSONField(json_dumps=orjson.dumps, json_loads=orjson.loads)
    result = JSONField(json_dumps=orjson.dumps, json_loads=orjson.loads)

    created = DateTimeField(default=datetime.datetime.utcnow, index=True)
    expires = DateTimeField(index=True, null=True)

    class Meta:
        database = db
        indexes = (
            # unique together
            (('fn_name', 'arguments'), True),
        )


MemoizedCall.create_table(True)


def memoize(remember="forever"):
    """
    Memoizing decorator
    todo: cache generators?
    """
    def decorator(fn):
        @functools.wraps(fn)
        def inner(*args, **kwargs):
            call_args = inspect.getcallargs(fn, *args, **kwargs)
            if remember.lower() == "forever":
                try:
                    result = (MemoizedCall
                              .select()
                              .where(MemoizedCall.fn_name == fn.__name__,
                                     MemoizedCall.arguments == call_args)
                              .get()
                              .result
                              )
                except MemoizedCall.DoesNotExist:
                    result = fn(**call_args)
                    MemoizedCall.insert(
                        fn_name=fn.__name__,
                        arguments=call_args,
                        result=result,
                        expires=None,
                    ).on_conflict_ignore().execute()
            else:
                try:
                    result = (MemoizedCall
                              .select()
                              .where(MemoizedCall.fn_name == fn.__name__,
                                     MemoizedCall.arguments == call_args,
                                     MemoizedCall.expires >= datetime.datetime.utcnow(),
                                     )
                              .get()
                              .result
                              )
                except MemoizedCall.DoesNotExist:
                    result = fn(**call_args)
                    expiry_date = dateparser.parse(remember,
                                                   settings={
                                                       'TIMEZONE': 'UTC',
                                                       'PREFER_DATES_FROM': 'future',
                                                   })
                    MemoizedCall.insert(
                        fn_name=fn.__name__,
                        arguments=call_args,
                        result=result,
                        expires=expiry_date,
                    ).on_conflict_replace().execute()
            return result
        return inner
    return decorator
