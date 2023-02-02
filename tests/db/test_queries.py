import pytest
from sqlalchemy import select, Select

from short_url.app.database import async_session
from short_url.db.models.url import TShortUrl
from short_url.db.queries import (
    get_source_url_from_db,
    create_short_url_in_db,
    remove_short_url_from_db
)


async def get_all():
    async with async_session() as session:
        query: Select = select(TShortUrl)
        return await session.execute(query)


@pytest.mark.asyncio
async def test_get_source_url_from_db(data):
    res = await get_source_url_from_db('test1')
    assert res.source_url == 'https://google.com'


@pytest.mark.asyncio
async def test_create_short_url_in_db():
    _all = await get_all()
    expected = len(_all.all()) + 1

    short_url = await create_short_url_in_db('http://very_long_url')

    _all = await get_all()
    assert len(_all.all()) == expected
    assert short_url


@pytest.mark.asyncio
async def test_remove_short_url_from_db(data):
    await remove_short_url_from_db('test1')

    for i in await get_all():
        for j in i:
            assert j.short_url != 'test1'
