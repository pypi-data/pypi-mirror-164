from pathlib import Path

from pydantic import BaseSettings

# user_config_dir in appdirs is weird on MacOS!
# hence, let's take home/.lndb
settings_dir = Path.home() / ".lndb"
settings_dir.mkdir(parents=True, exist_ok=True)
current_instance_settings_file = settings_dir / "current_instance.env"
current_user_settings_file = settings_dir / "current_user.env"


class InstanceSettingsStore(BaseSettings):
    storage_dir: str
    dbconfig: str
    schema_modules: str

    class Config:
        env_file = ".env"


class UserSettingsStore(BaseSettings):
    email: str
    password: str
    id: str
    handle: str

    class Config:
        env_file = ".env"


class Connector(BaseSettings):
    url: str
    key: str
