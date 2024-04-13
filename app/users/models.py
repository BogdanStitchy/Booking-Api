from sqlalchemy import Column, Integer, Date, ForeignKey, Computed, String, JSON

from app.db.base_model import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)

