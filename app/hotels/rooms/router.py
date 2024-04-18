from datetime import date
from fastapi_cache.decorator import cache

from app.hotels.router import router
from app.hotels.rooms.dao import RoomsDAO
from app.hotels.rooms.schemas import SRooms


@router.get("/{hotel_id}/rooms")
@cache(expire=60)
async def get_rooms(hotel_id: int, date_from: date, date_to: date) -> list[SRooms]:
    result = await RoomsDAO.get_all(hotel_id, date_from, date_to)
    return result
