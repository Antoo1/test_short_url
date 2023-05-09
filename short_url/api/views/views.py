from fastapi import APIRouter, status, Depends
from fastapi.responses import RedirectResponse
from fastapi_utils.cbv import cbv
from sqlalchemy.ext.asyncio import AsyncSession

from short_url.api.controllers.url_create import UrlController
from short_url.api.dependencies.dependencies import get_db_session
from short_url.api.serializers.short_url import ShortUrlCreate
from short_url.app.config import config

routes = APIRouter()


@cbv(routes)
class ShortUrl:

    db_session: AsyncSession = Depends(get_db_session)

    @routes.post('/short_url')
    async def create_short_url(self, short_url: ShortUrlCreate):
        return await UrlController(self.db_session).create_url(short_url)

    @routes.get('/short_url/{short_url}')
    async def source_url(self, short_url: str):
        return {'source_url': await UrlController(self.db_session).get_source_url(short_url)}

    @routes.api_route('/{path:path}', methods=list(map(str.upper, config.METHODS)))
    async def route_request(self, path: str):
        url = await UrlController(self.db_session).get_source_url(path)
        return RedirectResponse(url)

    @routes.delete('/short_url/{short_url}', status_code=status.HTTP_204_NO_CONTENT)
    async def remove_link(self, short_url: str):
        await UrlController(self.db_session).delete_short_url(short_url)
        return
