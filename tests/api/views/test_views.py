import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_short_url(client: AsyncClient, data):
    data = {'url': 'test1'}

    res = await client.post('/v1/short_url', json=data)

    assert isinstance(res.json(), str)
    assert res.status_code == 200
    assert len(res.json()) > 10
