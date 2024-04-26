from datetime import date

from fastapi_cache.decorator import cache
from pydantic import parse_obj_as

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBookingAdvancedData, SBookingWithRoomData
from app.exceptions import RoomCannotBeBooked, BookingsNotFoundException
from app.tasks.tasks import send_booking_confirmation_email
from app.users.dependencies import get_current_user
from app.users.models import Users
from fastapi import APIRouter, Depends, Response, status
from fastapi_versioning import version

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"]
)


@router.get("")
@version(1)
@cache(expire=60)
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBookingWithRoomData]:
    returning_value = await BookingDAO.get_all(user_id=user.id)

    if not returning_value:
        raise BookingsNotFoundException

    if "error" in returning_value:
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return returning_value


@router.post("/add_booking")
@version(1)
async def add_bookings(room_id: int, date_from: date, date_to: date,
                       user: Users = Depends(get_current_user)):
    booking_id = await BookingDAO.add(user.id, room_id, date_from, date_to)

    if not booking_id:
        raise RoomCannotBeBooked

    if isinstance(booking_id, dict):
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    advanced_booking_data = await BookingDAO.get_bookings_data_for_email(booking_id)
    advanced_booking_data = parse_obj_as(SBookingAdvancedData, advanced_booking_data).dict()
    send_booking_confirmation_email.delay(advanced_booking_data, user.email)

    return advanced_booking_data


@router.delete("/{booking_id}")
@version(1)
async def delete_booking(booking_id: int):
    await BookingDAO.delete(id=booking_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
