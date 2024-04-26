from datetime import date

from sqlalchemy import and_, func, join, or_, select
from sqlalchemy.sql.functions import coalesce

from app.bookings.models import Bookings
from app.dao.base import BaseDAO
from app.db.base_model import async_session_maker
from app.hotels.models import Hotels
from app.hotels.rooms.models import Rooms


class RoomsDAO(BaseDAO):
    model = Rooms

    @classmethod
    async def get_all(cls, hotel_id: int, date_from: date, date_to: date):
        async with async_session_maker() as session:
            query_find = and_(
                Hotels.id == hotel_id,
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

            booked_rooms = select(
                Rooms.id,
                (func.count(Rooms.id)).label("count_booked_rooms")
            ).where(
                query_find
            ).group_by(
                Rooms.id
            ).select_from(
                join(Hotels, Rooms, Rooms.hotel_id == Hotels.id)
                    .join(Bookings, Bookings.room_id == Rooms.id)
            ).cte("booked_rooms")

            get_rooms_left = select(
                Rooms.__table__,
                (func.coalesce(func.sum(Bookings.total_cost), 0)).label("total_cost"),
                (Rooms.quantity - coalesce(booked_rooms.c.count_booked_rooms, 0)).label("rooms_left")
            ).where(
                Rooms.hotel_id == hotel_id
            ).join(
                booked_rooms,
                booked_rooms.c.id == Rooms.id,
                isouter=True
            ).join(
                Bookings,
                Bookings.room_id == Rooms.id,
                isouter=True
            ).group_by(
                Rooms.id,
                Rooms.quantity,
                booked_rooms.c.count_booked_rooms
            ).order_by(
                Rooms.id
            )

            booked_rooms = await session.execute(get_rooms_left)
            booked_rooms = booked_rooms.mappings().all()

            return booked_rooms
