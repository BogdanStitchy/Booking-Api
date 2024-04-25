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


@pytest.mark.parametrize("hotel_id, status_code, expected_data", [
    (1, 200,
     {'id': 1, 'name': 'Cosmos Collection Altay Resort',
      'location': 'Республика Алтай, Майминский район, село Урлу-Аспак, Лесхозная улица, 20',
      'services': ['Wi-Fi', 'Бассейн', 'Парковка', 'Кондиционер в номере'], 'rooms_quantity': 15,
      'image_id': 1}),

    (2, 200,
     {'id': 2, 'name': 'Skala', 'location': 'Республика Алтай, Майминский район, поселок Барангол, Чуйская улица 40а',
      'services': ['Wi-Fi', 'Парковка'], 'rooms_quantity': 23, 'image_id': 2}),

    (12, 404, {}),
])
async def test_api_get_one_hotel(async_client, start_redis_for_method_with_cache,
                                 hotel_id, status_code, expected_data):
    response = await async_client.get(f"/hotels/{hotel_id}/1")
    if status_code == 200:
        assert response.json() == expected_data

    assert response.status_code == status_code
