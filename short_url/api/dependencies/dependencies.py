from typing import Generator

from sqlalchemy.ext.asyncio import AsyncSession

from short_url.app.database import engine, setup_async_session


async def get_db_session() -> Generator[AsyncSession, None, None]:
    async with setup_async_session(engine)() as session:
        yield session
