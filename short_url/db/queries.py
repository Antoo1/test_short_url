from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from short_url.db.models.url import TShortUrl


async def get_source_url_from_db(short_url: str, session: AsyncSession) -> TShortUrl:
    query = select(TShortUrl).where(TShortUrl.short_url == short_url)
    result = await session.execute(query)
    return result.scalars().one()


async def create_short_url_in_db(source_url: str, session: AsyncSession) -> str:
    new_url = TShortUrl(source_url=source_url)
    session.add(new_url)
    await session.commit()
    await session.refresh(new_url)
    return new_url.short_url


async def remove_short_url_from_db(short_url: str, session: AsyncSession):
    query = delete(TShortUrl).where(TShortUrl.short_url == short_url)
    await session.execute(query)
    await session.commit()
