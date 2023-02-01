from sqlalchemy.ext.asyncio import AsyncSession

from short_url.api.serializers.short_url import ShortUrlCreate



async def create_url(url: ShortUrlCreate, session: AsyncSession):
    new_url = _create_url(url.url)



async def get_source_url(url: str, session: AsyncSession):
    ...
