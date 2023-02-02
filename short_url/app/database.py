from typing import Callable

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from short_url.app.config import config

engine = create_async_engine(
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

async_session: Callable[[], AsyncSession] = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
)
