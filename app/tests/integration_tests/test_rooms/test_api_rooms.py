import pytest


@pytest.mark.parametrize("hotel_id, status_code, date_from, date_to, expected_count_rooms", [
    (1, 200, "2020-10-10", "2033-10-20", 2),

    (2, 200, "2023-10-10", "2023-10-20", 2),

    (12, 404, "2023-10-10", "2023-10-20", 10),
])
async def test_api_get_one_hotel(async_client, start_redis_for_method_with_cache,
                                 hotel_id, status_code, date_from, date_to, expected_count_rooms):
    response = await async_client.get(f"/hotels/{hotel_id}/rooms", params={
        "date_from": date_from,
        "date_to": date_to
    })
    print(f"{response.json()=}")
    print(f"{len(response.json())=}")
    if status_code == 200:
        assert len(response.json()) == expected_count_rooms

    assert response.status_code == status_code
