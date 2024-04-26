from datetime import date

from sqlalchemy import and_, func, insert, or_, select
from sqlalchemy.exc import SQLAlchemyError

from app.bookings.models import Bookings
from app.dao.base import BaseDAO
from app.db.base_model import async_session_maker
from app.hotels.models import Hotels
from app.hotels.rooms.models import Rooms
from app.logger import logger


class BookingDAO(BaseDAO):
    model = Bookings

    @classmethod
    async def add(cls,
                  user_id: int,
                  room_id: int,
                  date_from: date,
                  date_to: date):
        """
                WITH booked_rooms AS (
                            SELECT * FROM bookings
                              WHERE room_id = 1 AND
                                    (date_from >= '2023-05-15' AND date_from <= '2023-06-20')
                                 OR (date_from <= '2023-05-15' AND date_to > '2023-05-15')
                              )
        SELECT rooms.quantity - COUNT(booked_rooms.room_id) FROM rooms
        LEFT JOIN booked_rooms ON booked_rooms.room_id = rooms.id
        WHERE rooms.id = 1
        GROUP BY rooms.quantity, booked_rooms.room_id;
        """
        try:
            async with async_session_maker() as session:
                booked_rooms = select(Bookings).where(
                    and_(
                        Bookings.room_id == room_id,
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
                ).cte("booked_rooms")

                get_rooms_left = select(
                    (Rooms.quantity - func.count(booked_rooms.c.room_id)).label("rooms_left")
                ).select_from(Rooms).join(
                    booked_rooms, booked_rooms.c.room_id == Rooms.id, isouter=True
                ).where(Rooms.id == room_id).group_by(
                    Rooms.quantity, booked_rooms.c.room_id
                )

                rooms_left = await session.execute(get_rooms_left)
                rooms_left: int = rooms_left.scalar()

                if rooms_left > 0:
                    get_price = select(Rooms.price).filter_by(id=room_id)
                    price = await session.execute(get_price)
                    price: int = price.scalar()
                    add_booking = insert(Bookings).values(
                        room_id=room_id,
                        user_id=user_id,
                        date_from=date_from,
                        date_to=date_to,
                        price=price,
                    ).returning(Bookings.id)

                    new_booking = await session.execute(add_booking)
                    await session.commit()
                    new_booking = new_booking.scalar()
                    return new_booking
                else:
                    return None
        except (SQLAlchemyError, Exception) as error:
            if isinstance(error, SQLAlchemyError):
                msg = "Database Exc"
            if isinstance(error, Exception):
                msg = "Unknown Exc"
            msg += ": Cannot add booking"
            extra = {
                "user_id": user_id,
                "room_id": room_id,
                "date_from": date_from,
                "date_to": date_to
            }
            logger.error(msg, extra=extra, exc_info=True)
            return {"error": error.__str__()}

    @classmethod
    async def get_all(cls, user_id: int):
        try:
            async with async_session_maker() as session:
                query = select(cls.model.__table__,
                               Rooms.image_id,
                               Rooms.name,
                               Rooms.description,
                               Rooms.services
                               ).filter_by(user_id=user_id).join(Rooms)
                result = await session.execute(query)
                result = result.mappings().all()
                return result
        except (SQLAlchemyError, Exception) as error:
            if isinstance(error, SQLAlchemyError):
                msg = "Database Exc"
            if isinstance(error, Exception):
                msg = "Unknown Exc"
            msg += ": Cannot get all bookings"
            extra = {
                "user_id": user_id
            }
            logger.error(msg, extra=extra, exc_info=True)
            return {"error": error.__str__()}

    @classmethod
    async def get_bookings_data_for_email(cls, booking_id: int):
        try:
            async with async_session_maker() as session:
                query = select(cls.model.__table__,
                               Rooms.name.label("room_name"),
                               Hotels.name.label("hotel_name"),
                               Hotels.location,
                               ).where(Bookings.id == booking_id
                                       ).join(Rooms, Rooms.id == Bookings.room_id
                                              ).join(Hotels, Hotels.id == Rooms.hotel_id)
                result = await session.execute(query)
                result = result.mappings().fetchone()
                return result
        except (SQLAlchemyError, Exception) as error:
            if isinstance(error, SQLAlchemyError):
                msg = "Database Exc"
            if isinstance(error, Exception):
                msg = "Unknown Exc"
            msg += ": Cannot get data one booking"
            extra = {
                "booking_id": booking_id
            }
            logger.error(msg, extra=extra, exc_info=True)
            return {"error": error.__str__()}
