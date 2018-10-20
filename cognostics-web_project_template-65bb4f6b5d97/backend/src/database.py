import logging
import time

from psycopg2.extensions import TransactionRollbackError
from sqlalchemy.exc import OperationalError
from flask_sqlalchemy import SQLAlchemy


class TransactionFailed(Exception):
    pass


class SerializableSQLAlchemy(SQLAlchemy):
    """Subclass of SQLAlchemy in order to inject options into the create_engine function.

    Set the isolation_level to SERIALIZABLE in order to guarantee full transaction isolation at the expense of some
    performance loss when dealing with many concurrent requests. Since the number of concurrent users of the
    application is small, this is a good trade off.
    """

    def apply_driver_hacks(self, app, info, options):
        """Set options that are passed to create_engine"""
        options.update({"isolation_level": "SERIALIZABLE"})
        super().apply_driver_hacks(app, info, options)


# This is the singleton that will be used in order to access the database from the rest of the application
db = SerializableSQLAlchemy()


def retry_transaction(session=db.session, retry_count=5, retry_delay=0.1):
    """Decorator factory to retry transactions a number of times in case of errors due to concurrent access

    If f is a function containing all the queries/updates etc of a database transaction, it can be decorated like this
    @retry_transaction()
    def f():
        ...

    By default this decorator assumes that all transactions are done via the context-local db.session. If the decorated
    function uses some other session object, it may be passed as an optional parameter. The maximum number of retries
    and the delay between retries may also be set e.g.

    @retry_transaction(session=my_session, retry_count=3, retry_delay=1)
    def f():
        ...

    In order for this function to work properly it is important that sqlalchemy.exc.OperationalError are not
    caught and are raised to the top level.
    """

    def decorator(f):
        def decorated_f(*args, **kwargs):
            transaction_successful = False
            for i in range(retry_count):
                try:
                    f(*args, **kwargs)
                    session.commit()
                    transaction_successful = True
                    break
                except OperationalError as e:
                    if isinstance(e.__cause__, TransactionRollbackError):
                        session.rollback()
                        logging.warning("Transaction retry due to concurrent update")
                        time.sleep(retry_delay)
                    else:
                        raise

            if not transaction_successful:
                logging.error("Transaction retry count exceeded. Transaction failed")
                raise TransactionFailed

        return decorated_f

    return decorator
