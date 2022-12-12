from sqlalchemy import event
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import Query, sessionmaker

from core.models import TimestampedModel
from core.settings import app_settings

connection_str = f"postgresql+psycopg2://{app_settings.db_username}:{app_settings.db_password}@{app_settings.db_host}:{app_settings.db_port}/{app_settings.db_name}"

engine = create_engine(connection_str)
SessionFactory = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def get_session():
    session = SessionFactory()
    yield session


@event.listens_for(Query, "before_compile", retval=True)
def filter_out_soft_deleted_rows(query: Query):
    """
    Before the query is compiled, check if the entity is an instance of `TimestampedModel` and if so,
    filter out any rows that have a non-null `deleted_at` column

    :param query: The query object that is being compiled
    :type query: Query
    :return: The query object is being returned.
    """
    for desc in query.column_descriptions:
        if issubclass(desc["type"], TimestampedModel):
            entity = desc["entity"]
            query = query.filter(entity.deleted_at == None)
    return query


__all__ = ["get_session", "connection_str"]
