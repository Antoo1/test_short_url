import pytest_asyncio

from sqlalchemy.ext.asyncio import AsyncSession
from asgi_lifespan import LifespanManager
from httpx import AsyncClient

from short_url.app.config import config as c
from short_url.app.database import async_session
from short_url.app.fastapi import create_app
from short_url.app.logging_configuration import init_logging
from .fixtures.fixtures import *


if c.INIT_LOGGING:
    init_logging()


@pytest_asyncio.fixture(scope='session')
async def app():
    app = create_app()
    async with LifespanManager(app):
        yield app


@pytest_asyncio.fixture
async def client(app) -> AsyncClient:
    async with AsyncClient(app=app, base_url='http://test') as ac:
        yield ac


@pytest_asyncio.fixture(scope='session')
async def db() -> AsyncSession:
    async with async_session() as session:
        yield session
