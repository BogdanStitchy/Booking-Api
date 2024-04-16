from datetime import date
from fastapi import APIRouter

from app.hotels.schemas import SHotels

from app.hotels.dao import HotelsDAO

router = APIRouter(
    prefix="/hotels",
    tags=["Отели"]
)


@router.get("/{location}")
async def get_hotels(location: str, date_from: date, date_to: date) -> list[SHotels]:
    result = await HotelsDAO.get_all(location, date_from, date_to)
    print(f"{result=}")
    return result
