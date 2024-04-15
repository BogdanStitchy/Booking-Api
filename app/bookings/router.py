from datetime import date

from fastapi import APIRouter, Depends

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking
from app.exceptions import RoomCannotBeBooked
from app.users.models import Users
from app.users.dependencies import get_current_user

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"]
)


@router.get("/get_bookings")
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBooking]:
    returning_value = await BookingDAO.get_all(user_id=user.id)
    return returning_value


@router.post("/add_booking")
async def add_bookings(room_id: int, date_from: date, date_to: date,
                       user: Users = Depends(get_current_user)):
    booking = await BookingDAO.add(user.id, room_id, date_from, date_to)
    print(f"{booking=}")
    if not booking:
        raise RoomCannotBeBooked
