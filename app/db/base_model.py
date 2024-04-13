from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from config import config


engine = create_async_engine(config.DATABASE_URL)

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)  # expire_on_commit - если
# исполнили транзакцию, чтобы не исчезала фабрика сессий


class Base(DeclarativeBase):
    pass
