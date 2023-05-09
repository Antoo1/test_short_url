import pytest
import sqlalchemy
from sqlalchemy import select

from short_url.db.models.url import TShortUrl
from short_url.db.queries import (
    get_source_url_from_db,
    create_short_url_in_db,
    remove_short_url_from_db
)
from tests.fixtures.fixtures import data


@pytest.mark.asyncio
async def test_get_source_url_from_db(data, db):
    res = await get_source_url_from_db('test1', db)
    assert res.source_url == 'https://google.com'


@pytest.mark.asyncio
async def test_create_short_url_in_db(db):
    async with db() as _db:
        short_url = await create_short_url_in_db('http://very_long_url', _db)

        query = select(TShortUrl).where(TShortUrl.source_url == 'http://very_long_url')
        res = await db.execute(query)
        res = res.scalar_one()

    assert res
    assert short_url == res.short_url


@pytest.mark.asyncio
async def test_remove_short_url_from_db(data, db):
    async with db() as _db:
        query = select(TShortUrl).where(TShortUrl.short_url == 'test1')
        before_action = (await db.execute(query)).scalar_one()
        assert before_action

        await remove_short_url_from_db('test1', db)

        query = select(TShortUrl).where(TShortUrl.short_url == 'test1')
        with pytest.raises(sqlalchemy.exc.NoResultFound):
            (await db.execute(query)).scalar_one()
