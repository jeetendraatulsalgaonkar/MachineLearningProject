from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

from com.demo.visa.constants import PGUSER, PGPASSWORD, PGHOST, PGDB, PGPORT


# use engine.getEngine(settings['pguser'], settings['pgpassword'], settings['pghost'], ...)
# to get engine, can be verified using engine.url
def get_engine(user, password, database, host, port):
    url = f"postgresql://{user}:{password}@{host}:{port}/{database}"
    if not database_exists(url):
        create_database(url)
    return create_engine(url, pool_size=50, echo=False)


def get_engine_from_settings():
    return get_engine(
        PGUSER,
        PGPASSWORD,
        PGDB,
        PGHOST,
        PGPORT
    )


def get_session():
    return sessionmaker(bind=get_engine_from_settings())()

# session = get_session()
