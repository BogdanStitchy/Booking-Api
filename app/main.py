from time import time
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_versioning import VersionedFastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from redis import asyncio as aioredis
from sqladmin import Admin
import sentry_sdk

from app.admin_panel.auth import authentication_backend
from app.admin_panel.views import BookingsAdmin, HotelsAdmin, RoomsAdmin, UsersAdmin
from app.bookings.router import router as router_bookings
from app.db.base_model import engine
from app.hotels.rooms.router import router as router_rooms
from app.hotels.router import router as router_hotels
from app.images.router import router as router_images
from app.importer.router import router as router_import
from app.logger import logger
from app.pages.router import router as router_pages
from app.users.router import router as router_users
from config.config import HOST_REDIS, SENTRY_DNS

app = FastAPI()

sentry_sdk.init(
    dsn=SENTRY_DNS,
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

app.include_router(router_users)
app.include_router(router_bookings)
app.include_router(router_hotels)
app.include_router(router_rooms)

app.include_router(router_pages)
app.include_router(router_images)
app.include_router(router_import)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  # отвечает за куки, с каждым запросом посылается кука хранящася
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content_Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)


@app.on_event("startup")
async def startup():
    redis = await aioredis.from_url(f"redis://{HOST_REDIS}", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="cache")


# app = VersionedFastAPI(app,
#                        version_format='{major}',
#                        prefix_format='/v{major}',
#                        description='Добро пожаловать на страницу документации проекта.'
#                                    '<br>На текущий момент доступна одна версия проекта.'
#                        # middleware=[
#                        #     Middleware(SessionMiddleware, secret_key='')
#                        # ]
#                        )

instrumentator = Instrumentator(
    should_group_status_codes=False,  # не группировать статусы ответа
    excluded_handlers=[".*admin.*", "/metrics"],  # игнорируемые эндпоинты
)
instrumentator.instrument(app).expose(app)  # Prometheus

admin = Admin(app, engine, authentication_backend=authentication_backend)

admin.add_view(UsersAdmin)
admin.add_view(BookingsAdmin)
admin.add_view(HotelsAdmin)
admin.add_view(RoomsAdmin)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time()
    response = await call_next(request)
    process_time = time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    logger.info("Request execution time", extra={
        "process_time": round(process_time, 4)
    })
    return response


app.mount("/static", StaticFiles(directory="app/static"), "static")
