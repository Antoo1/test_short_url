from short_url.api.serializers.short_url import ShortUrlCreate
from short_url.db.queries import get_source_url_from_db, remove_short_url_from_db, create_short_url_in_db


async def create_url(url: ShortUrlCreate):
    return await create_short_url_in_db(url.url)


async def get_source_url(url: str):
    return (await get_source_url_from_db(url)).source_url


async def delete_short_url(url: str):
    return await remove_short_url_from_db(url)
