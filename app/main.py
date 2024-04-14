from fastapi import FastAPI, Query, Depends
from typing import Union
from datetime import date
from pydantic import BaseModel

from app.bookings.router import router as router_bookings
from app.users.router import router as router_users

app = FastAPI()

app.include_router(router_users)
app.include_router(router_bookings)


class SHotel(BaseModel):
    address: str
    name: str
    stars: int


class SSearchArgs:
    def __init__(self,
                 location: str,
                 date_from: date,
                 date_to: date,
                 has_spa: Union[bool] = None,
                 stars: Union[int] = Query(default=None, ge=1, le=5)
                 ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.stars = stars


@app.get("hotels")
def get_hotels(
        search_args: SSearchArgs = Depends()
):
    hotels = [
        {
            "address": "ул. Передовая, Москва",
            "name": "Main Hotel",
            "stars": 5
        }
    ]
    return search_args
    #     {
    #     "location": location,
    #     "date_from": date_from,
    #     "date_to": date_to,
    #     "has_spa": has_spa,
    #     "stars": stars
    # }


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date

# @app.post("bookings")
# def add_booking(booking: SBooking):
#     pass
