from typing import Generator

from sqlalchemy.ext.asyncio import AsyncSession

from short_url.api.controllers.url_create import get_source_url
from short_url.app.database import async_session


async def get_db() -> Generator[AsyncSession, None, None]:
    async with async_session() as session:
        yield session


async def get_source_url_dep(short_url) -> str:
    session = get_db()
    return await get_source_url(short_url, session)
