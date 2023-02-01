from fastapi import APIRouter, Request, Depends
from fastapi.responses import RedirectResponse

from short_url.api.controllers.url_create import create_url, get_source_url
from short_url.api.dependencies.short_url import get_source_url_dep, get_db
from short_url.api.serializers.short_url import ShortUrlCreate
from short_url.app.config import config

routes = APIRouter()


@routes.post('/short_url')
async def create_short_url(short_url: ShortUrlCreate):
    return await create_url(short_url)

#
# @routes.get('short_url/{short_url}')
# async def source_url(short_url: str, db: Depends(get_db)):
#     return {'source_url': await get_source_url(short_url, db)}
#

@routes.api_route('/lala', methods=list(map(str.upper, config.METHODS)))
# async def route_request(r: Request, source_url=Depends(get_source_url_dep)):
async def route_request(r: Request):
    return RedirectResponse('https://ya.ru')


@routes.delete('short_url/{short_url}')
async def remove_link():
    ...
