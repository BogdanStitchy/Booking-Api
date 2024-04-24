from datetime import datetime
from app.bookings.dao import BookingDAO


async def test_add_and_get_booking():
    new_booking_id = await BookingDAO.add(
        user_id=2,
        room_id=2,
        date_from=datetime.strptime("2024-06-10", "%Y-%m-%d"),
        date_to=datetime.strptime("2024-06-20", "%Y-%m-%d")
    )
    assert new_booking_id == 4

    new_booking = await BookingDAO.find_by_id(new_booking_id)
    assert new_booking is not None
