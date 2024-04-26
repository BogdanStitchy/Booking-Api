from datetime import date

from fastapi import Response, status
from fastapi_cache.decorator import cache

from app.hotels.exceptions import IncorrectHotelIdException, IncorrectTimePeriodException
from app.hotels.rooms.dao import RoomsDAO
from app.hotels.rooms.schemas import SRooms
from app.hotels.router import router


@router.get("/{hotel_id}/rooms")
@cache(expire=60)
async def get_rooms(hotel_id: int, date_from: date, date_to: date) -> list[SRooms]:
    if date_from > date_to:
        raise IncorrectTimePeriodException

    result = await RoomsDAO.get_all(hotel_id, date_from, date_to)
    if result in ([], None):
        raise IncorrectHotelIdException

    if "error" in result:
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return result
