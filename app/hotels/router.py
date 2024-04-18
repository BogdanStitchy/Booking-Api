from datetime import date
from fastapi import APIRouter
from fastapi_cache.decorator import cache

from app.hotels.schemas import SHotelsWithRoomsLeft, SHotels

from app.hotels.dao import HotelsDAO

router = APIRouter(
    prefix="/hotels",
    tags=["Отели"]
)


@router.get("/{location}")
@cache(expire=60)
async def get_hotels(location: str, date_from: date, date_to: date) -> list[SHotelsWithRoomsLeft]:
    result = await HotelsDAO.get_all(location, date_from, date_to)
    return result


@router.get("/{hotel_id}/1")
async def get_one_hotel(hotel_id: int) -> SHotels:
    result = await HotelsDAO.find_by_id(hotel_id)
    print(f"{result=}")
    return result
