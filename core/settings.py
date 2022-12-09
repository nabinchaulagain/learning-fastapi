from pydantic import BaseSettings


class AppSettings(BaseSettings):
    db_username: str
    db_password: str
    db_port: int
    db_name: str
    db_host: str

    class Config:
        env_file = ".env"


app_settings = AppSettings()

__all__ = ["app_settings"]
