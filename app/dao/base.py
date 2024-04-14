from sqlalchemy import select
from app.db.base_model import async_session_maker


class BaseDAO:
    model = None

    @classmethod
    async def find_by_id(cls, model_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_one_or_none(cls, **filer_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filer_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def get_all(cls, **filer_by):
        async with async_session_maker() as session:
            query = select(cls.model.__table__).filter_by(**filer_by)
            result = await session.execute(query)
            result = result.mappings().all()
            return result
