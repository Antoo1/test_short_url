import asyncio
from unittest.mock import patch

import pytest

from sqlalchemy.ext.asyncio import AsyncSession, async_scoped_session
from asgi_lifespan import LifespanManager
from httpx import AsyncClient
from sqlalchemy.orm import sessionmaker

from short_url.app.config import config as c
from short_url.app.database import _setup_db_engine
from short_url.app.fast_api import create_app
from short_url.app.logging_configuration import init_logging


if c.INIT_LOGGING:
    init_logging()


def scopefunc():
    return ''


TestDBSession = async_scoped_session(
    session_factory=sessionmaker(
        class_=AsyncSession,
        autoflush=True,
        autocommit=False,
        expire_on_commit=False,
    ),
    scopefunc=scopefunc
)


@pytest.fixture(scope='session')
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope='session')
async def app():
    app = create_app()
    async with LifespanManager(app):
        yield app


@pytest.fixture(scope='session')
async def client(app) -> AsyncClient:
    async with AsyncClient(app=app, base_url='http://test') as ac:
        yield ac


@pytest.fixture(scope='session')
async def db_engine():
    db_engine = _setup_db_engine()

    yield db_engine

    await db_engine.dispose()


@pytest.fixture
async def db(db_engine):
    connection = await db_engine.connect()
    TestDBSession.configure(bind=connection)
    transaction = await connection.begin()

    def setup_db_session(*args, **kwargs):
        return TestDBSession
    with patch('short_url.api.dependencies.dependencies.setup_async_session', setup_db_session):
        yield TestDBSession

    await transaction.rollback()
    await connection.close()
    await TestDBSession.remove()
