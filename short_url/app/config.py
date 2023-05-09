import os
from enum import Enum

from pydantic import BaseModel

from short_url.utils.utils import ConfigFactory


ENVIRONMENT = os.environ.get('ENVIRONMENT', 'local')
CONFIG_FILE = os.environ.get('CONFIG_FILE', f'./config/{ENVIRONMENT}.yml')


class Environment(str, Enum):
    LOCAL = 'LOCAL'
    TEST = 'TEST'


class Config(BaseModel):
    APP_NAME: str
    DEBUG: bool = False
    INIT_LOGGING: str
    LOG_LEVEL: str
    ENVIRONMENT: str
    DB_URL: str
    DB_POOL_SIZE: int

    METHODS: list


config: Config = ConfigFactory(Config).from_file(CONFIG_FILE)