from celery import Celery
from config.config import HOST_REDIS

celery = Celery(
    "tasks",
    broker=f"redis://{HOST_REDIS}",
    include="app.tasks.tasks"
)
