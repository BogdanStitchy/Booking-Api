from datetime import date

from sqlalchemy import and_, func, join, or_, select
from sqlalchemy.sql.functions import coalesce

from app.bookings.models import Bookings
from app.dao.base import BaseDAO
from app.db.base_model import async_session_maker
from app.hotels.models import Hotels
from app.hotels.rooms.models import Rooms


class HotelsDAO(BaseDAO):
    model = Hotels

    @classmethod
    async def get_all(cls, location: str, date_from: date, date_to: date):
        async with async_session_maker() as session:
            query_find = and_(
                Hotels.location.ilike(f"%{location}%"),
                or_(
                    and_(
                        Bookings.date_from >= date_from,
                        Bookings.date_from <= date_to
                    ),
                    and_(
                        Bookings.date_from <= date_from,
                        Bookings.date_to > date_from
                    )
                )
            )

            booked_rooms_in_hotel = select(
                Hotels.id,
                (func.count(Rooms.id)).label("count_booked_rooms")
            ).where(
                query_find
            ).group_by(
                Hotels.id
            ).select_from(
                join(Hotels, Rooms, Rooms.hotel_id == Hotels.id)
                    .join(Bookings, Bookings.room_id == Rooms.id)
            ).cte("booked_rooms_in_hotel")

            get_hotels_left = select(
                Hotels.id,
                Hotels.name,
                Hotels.location,
                Hotels.services,
                Hotels.rooms_quantity,
                Hotels.image_id,
                (Hotels.rooms_quantity - coalesce(booked_rooms_in_hotel.c.count_booked_rooms, 0)).label("rooms_left")
            ).where(
                Hotels.location.ilike(f"%{location}%"),
                # query_find
            ).join(
                booked_rooms_in_hotel,
                booked_rooms_in_hotel.c.id == Hotels.id,
                isouter=True
            ).group_by(
                Hotels.id,
                Hotels.rooms_quantity,
                booked_rooms_in_hotel.c.count_booked_rooms
            ).having(
                (Hotels.rooms_quantity - coalesce(booked_rooms_in_hotel.c.count_booked_rooms, 0)) > 0
            ).order_by(
                Hotels.id
            )

            left_hotels = await session.execute(get_hotels_left)
            left_hotels = left_hotels.mappings().all()

            return left_hotels
