from datetime import date, datetime, timedelta
from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.bookings.router import add_bookings, get_bookings
from app.hotels.rooms.router import get_rooms
from app.hotels.router import get_one_hotel, get_hotels
from app.pages.utils import format_number_thousand_separator, get_month_days

router = APIRouter(
    prefix="/pages",
    tags=["Фронтенд"]
)

templates = Jinja2Templates(directory="app/templates")


@router.get("/hotels")
async def get_hotels_page(
        request: Request,
        hotels=Depends(get_hotels)
):
    return templates.TemplateResponse(
        name="Hotels.html",
        context={"request": request, "hotels": hotels})


@router.get("/login", response_class=HTMLResponse)
async def get_login_page(request: Request):
    return templates.TemplateResponse("auth/login.html", {"request": request})


@router.get("/register", response_class=HTMLResponse)
async def get_register_page(request: Request):
    return templates.TemplateResponse("auth/register.html", {"request": request})

