# transaction and transactional decorators
from contextlib import contextmanager

from boltons.funcutils import wraps

from com.demo.visa.config.session_management import session_context_var, get_session


@contextmanager
def transaction():
    session = session_context_var.get()
    if session is None:
        session = get_session()
        session_context_var.set(session)

    is_nested = session.in_transaction()

    try:
        if is_nested:
            savepoint = session.begin_nested()
            yield savepoint
        else:
            session.begin()
            yield session

        if is_nested:
            savepoint.commit()
        else:
            session.commit()
            session.close()
    except Exception as e:
        if is_nested:
            savepoint.rollback()
        else:
            session.rollback()
            session.close()
        raise
    finally:
        if not is_nested:
            session_context_var.set(None)


def transactional(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with transaction():
            return func(*args, **kwargs)

    return wrapper
