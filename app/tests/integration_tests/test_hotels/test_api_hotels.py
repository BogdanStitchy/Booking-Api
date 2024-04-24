import pytest


@pytest.mark.parametrize("date_from, date_to, status_code", [
    ("2027-06-01", "2027-06-20", 200),
    ("2020-01-01", "2030-01-01", 400),
    ("2030-01-01", "2020-01-01", 400),
])
async def test_api_get_hotels(async_client, start_redis_for_method_with_cache,
                              date_from, date_to, status_code):
    response = await async_client.get("/hotels/Республика", params={
        "date_from": date_from,
        "date_to": date_to
    })

    assert response.status_code == status_code
