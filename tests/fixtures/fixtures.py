import pytest_asyncio

from short_url.db.models.url import TShortUrl


@pytest_asyncio.fixture(scope='session')
async def data(db):
    data = [
        TShortUrl(source_url='https://google.com', short_url='test1'),
        TShortUrl(source_url='https://ya.ru', short_url='test2'),
    ]
    db.add_all(data)
    await db.commit()
    db.expunge_all()
