from datetime import date
from fastapi import APIRouter, Depends, status, Response
from fastapi_cache.decorator import cache
from pydantic import parse_obj_as

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBookingWithRoomData, SBookingAdvancedData
from app.exceptions import RoomCannotBeBooked
from app.users.models import Users
from app.users.dependencies import get_current_user

from app.tasks.tasks import send_booking_confirmation_email

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"]
)


@router.get("")
@cache(expire=60)
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBookingWithRoomData]:
    returning_value = await BookingDAO.get_all(user_id=user.id)
    return returning_value


@router.post("/add_booking")
async def add_bookings(room_id: int, date_from: date, date_to: date,
                       user: Users = Depends(get_current_user)):
    booking_id = await BookingDAO.add(user.id, room_id, date_from, date_to)
    if not booking_id:
        raise RoomCannotBeBooked

    advanced_booking_data = await BookingDAO.get_bookings_data_for_email(booking_id)
    advanced_booking_data = parse_obj_as(SBookingAdvancedData, advanced_booking_data).dict()
    send_booking_confirmation_email.delay(advanced_booking_data, user.email)

    return advanced_booking_data


@router.delete("/{booking_id}")
async def delete_booking(booking_id: int):
    await BookingDAO.delete(id=booking_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
