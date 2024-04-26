from datetime import date

from fastapi_cache.decorator import cache

from app.hotels.dao import HotelsDAO
from app.hotels.exceptions import (
    IncorrectDurationTimeException,
    IncorrectHotelIdException,
    IncorrectTimePeriodException,
)
from app.hotels.schemas import SHotels, SHotelsWithRoomsLeft
from fastapi import APIRouter

router = APIRouter(
    prefix="/hotels",
    tags=["Отели"]
)


@router.get("/{location}")
@cache(expire=60)
async def get_hotels(location: str, date_from: date, date_to: date) -> list[SHotelsWithRoomsLeft]:
    if date_from > date_to:
        raise IncorrectTimePeriodException
    if (date_to - date_from).days > 100:
        raise IncorrectDurationTimeException
    result = await HotelsDAO.get_all(location, date_from, date_to)
    return result


@router.get("/{hotel_id}/1")
async def get_one_hotel(hotel_id: int) -> SHotels:
    result = await HotelsDAO.find_by_id(hotel_id)
    if result is None:
        raise IncorrectHotelIdException
    return result
