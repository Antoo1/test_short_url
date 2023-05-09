from typing import Callable

from sqlalchemy.engine import Engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from short_url.app.config import config
from short_url.utils.lazy_init_wrapper import LazyInitWrapper


def _setup_db_engine() -> Engine:
    return create_async_engine(
        config.DB_URL,
        pool_pre_ping=True,
        pool_recycle=3600,
        pool_size=config.DB_POOL_SIZE,
        max_overflow=0,
        connect_args={
            'command_timeout': 60,
            'server_settings': {
                'application_name': config.APP_NAME
            }
        },
        echo=config.DEBUG,
    )


def setup_async_session(db_engine: Engine) -> Callable[[], AsyncSession]:
    return sessionmaker(
        bind=db_engine,
        class_=AsyncSession,
        autocommit=False,
        autoflush=False,
        expire_on_commit=False,
    )


engine = LazyInitWrapper(_setup_db_engine)
