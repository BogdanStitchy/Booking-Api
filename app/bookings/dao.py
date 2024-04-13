from sqlalchemy import select

from app.dao.base import BaseDAO
from app.bookings.models import Bookings
from app.db.base_model import async_session_maker


class BookingDAO(BaseDAO):
    model = Bookings

    @classmethod
    async def get_all(cls):
        async with async_session_maker() as session:
            query = select(Bookings)
            bookings = await session.execute(query)
            return bookings.mappings().all()
