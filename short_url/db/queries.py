from sqlalchemy import select, delete

from short_url.app.database import async_session
from short_url.db.models.url import TShortUrl


async def get_source_url_from_db(short_url: str) -> TShortUrl:
    query = select(TShortUrl).where(TShortUrl.short_url == short_url)
    async with async_session() as session:
        result = await session.execute(query)
        return result.scalars().one()


async def create_short_url_in_db(source_url: str) -> str:
    async with async_session() as session:
        new_url = TShortUrl(source_url=source_url)
        session.add(new_url)
        await session.commit()
        return new_url.short_url


async def remove_short_url_from_db(short_url: str):
    async with async_session() as session:
        query = delete(TShortUrl).where(TShortUrl.short_url == short_url)
        await session.execute(query)
        await session.commit()
