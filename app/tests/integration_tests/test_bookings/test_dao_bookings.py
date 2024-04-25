from datetime import datetime, date
import pytest
from app.bookings.dao import BookingDAO


@pytest.mark.parametrize("expected_id", [
    4, 5, 6
])
async def test_add_and_get_booking(expected_id):
    new_booking_id = await BookingDAO.add(
        user_id=2,
        room_id=2,
        date_from=datetime.strptime("2024-06-10", "%Y-%m-%d"),
        date_to=datetime.strptime("2024-06-20", "%Y-%m-%d")
    )
    assert new_booking_id == expected_id

    new_booking = await BookingDAO.find_by_id(new_booking_id)
    assert new_booking is not None


@pytest.mark.parametrize("id_booking, expected_data_booking", [
    (1, {'id': 1, 'room_id': 1, 'user_id': 1, 'date_from': date(2023, 6, 15),
         'date_to': date(2023, 6, 30), 'price': 24500, 'total_cost': 367500, 'total_days': 15,
         'room_name': 'Улучшенный с террасой и видом на озеро', 'hotel_name': 'Cosmos Collection Altay Resort',
         'location': 'Республика Алтай, Майминский район, село Урлу-Аспак, Лесхозная улица, 20'}),

    (2, {'id': 2, 'room_id': 2, 'user_id': 1, 'date_from': date(2023, 4, 1),
         'date_to': date(2023, 4, 19), 'price': 4300, 'total_cost': 77400, 'total_days': 18,
         'room_name': 'Делюкс Плюс', 'hotel_name': 'Cosmos Collection Altay Resort',
         'location': 'Республика Алтай, Майминский район, село Урлу-Аспак, Лесхозная улица, 20'})
])
async def test_get_bookings(id_booking, expected_data_booking):
    booking = await BookingDAO.get_bookings_data_for_email(id_booking)
    assert booking == expected_data_booking


@pytest.mark.parametrize("id_booking", [1, 2, 3])
async def test_delete_booking(id_booking):
    await BookingDAO.delete(id=id_booking)
    booking = await BookingDAO.get_bookings_data_for_email(id_booking)
    assert booking is None

