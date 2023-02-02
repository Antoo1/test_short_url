from fastapi import APIRouter, status
from fastapi.responses import RedirectResponse

from short_url.api.controllers.url_create import create_url, get_source_url, delete_short_url
from short_url.api.serializers.short_url import ShortUrlCreate
from short_url.app.config import config

routes = APIRouter()


@routes.post('/short_url')
async def create_short_url(short_url: ShortUrlCreate):
    return await create_url(short_url)


@routes.get('/short_url/{short_url}')
async def source_url(short_url: str):
    return {'source_url': await get_source_url(short_url)}


@routes.api_route('/{path:path}', methods=list(map(str.upper, config.METHODS)))
async def route_request(path: str):
    url = await get_source_url(path)
    return RedirectResponse(url)


@routes.delete('/short_url/{short_url}', status_code=status.HTTP_204_NO_CONTENT)
async def remove_link(short_url: str):
    await delete_short_url(short_url)
    return
