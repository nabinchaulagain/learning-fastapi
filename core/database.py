from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

from core.settings import app_settings

engine = create_engine(
    f"postgresql+psycopg2://{app_settings.db_username}:{app_settings.db_password}@{app_settings.db_host}:{app_settings.db_port}/{app_settings.db_name}",
    echo=True,
)
SessionFactory = sessionmaker(bind=engine)


def get_session():
    session = SessionFactory()
    yield session


__all__ = ["get_session"]
