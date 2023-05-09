from sqlalchemy.ext.asyncio import AsyncSession

from short_url.api.serializers.short_url import ShortUrlCreate
from short_url.db.queries import get_source_url_from_db, remove_short_url_from_db, create_short_url_in_db


class BaseDBContoller:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args, **kwargs):
        await self.db_session.commit()


class UrlController(BaseDBContoller):
    async def create_url(self, url: ShortUrlCreate):
        return await create_short_url_in_db(url.url, self.db_session)

    async def get_source_url(self, url: str):
        return (await get_source_url_from_db(url, self.db_session)).source_url

    async def delete_short_url(self, url: str):
        return await remove_short_url_from_db(url, self.db_session)
