from app.tasks.celery import celery
from PIL import Image
from pathlib import Path


@celery.task
def process_pic(path: str):
    im_path = Path(path)
    im = Image.open(im_path)
    im_resized = im.resize((1000, 500), Image.Resampling.BILINEAR)
    im_resized_mini = im.resize((200, 100), Image.Resampling.BILINEAR)
    im_resized.save(f"app/static/images/resized_1000_500_{im_path.name}")
    im_resized_mini.save(f"app/static/images/resized_200_100_{im_path.name}")
