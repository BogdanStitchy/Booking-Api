import pytest
from httpx import AsyncClient


@pytest.mark.parametrize("booked_room, status_code", [
    (3, 200),
    (4, 200),
    (5, 200),
    (6, 200),
    (7, 200),
    (8, 200),
    (9, 200),
    (10, 200),
    (10, 409),
    (10, 409)
])
async def test_api_add_and_get_booking(async_client_authenticated: AsyncClient, start_redis_for_method_with_cache,
                                       booked_room, status_code):
    response = await async_client_authenticated.post("/bookings/add_booking", params={
        "room_id": 4,
        "date_from": "2030-05-01",
        "date_to": "2030-05-10"
    })
    assert response.status_code == status_code

    response = await async_client_authenticated.get("/bookings")

    assert len(response.json()) == booked_room


async def test_delete_and_get_booking(async_client_authenticated: AsyncClient, start_redis_for_method_with_cache):
    response_bookings = await async_client_authenticated.get("/bookings")
    count_bookings = len(response_bookings.json())
    for i in range(1, count_bookings + 1):
        response_delete = await async_client_authenticated.delete(f"/bookings/{i}")
        assert response_delete.status_code == 204
    response_bookings = await async_client_authenticated.get("/bookings")
    assert len(response_bookings.json()) == 0
