from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from local_settings import postgresql as settings


# use engine.getEngine(settings['pguser'], settings['pgpassword'], settings['pghost'], ...)
# to get engine, can be verified using engine.url
def get_engine(user, password, database, host, port):
    url = f"postgresql://{user}:{password}@{host}:{port}/{database}"
    if not database_exists(url):
        create_database(url)
    return create_engine(url, pool_size=50, echo=False)


def get_engine_from_settings():
    keys = ['pguser', 'pgpassword', 'pghost', 'pgport', 'pgdb']
    if not all(key in keys for key in settings.keys()):
        raise Exception('Missing required settings')

    return get_engine(
        settings['pguser'],
        settings['pgpassword'],
        settings['pghost'],
        settings['pgport'],
        settings['pgdb']
    )


def get_session():
    return sessionmaker(bind=get_engine_from_settings())()

# session = get_session()
