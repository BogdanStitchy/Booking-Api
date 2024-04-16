from datetime import date

from sqlalchemy import and_, or_, func, join, select
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
                (func.sum(Bookings.total_cost)).label("total_cost"),
                (Rooms.quantity - coalesce(booked_rooms.c.count_booked_rooms, 0)).label("rooms_left")
            ).where(
                query_find
            ).join(
                booked_rooms,
                booked_rooms.c.id == Rooms.id
            ).join(
                Bookings,
                Bookings.room_id == Rooms.id
            ).group_by(
                Rooms.id,
                Rooms.quantity,
                booked_rooms.c.count_booked_rooms
            ).order_by(
                Rooms.id
            )

            query = select(booked_rooms)
            booked_rooms = await session.execute(get_rooms_left)
            booked_rooms = booked_rooms.mappings().all()

            return booked_rooms
