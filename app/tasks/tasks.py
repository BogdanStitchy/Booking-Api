import smtplib
from pathlib import Path

from PIL import Image
from pydantic import EmailStr

from app.tasks.celery import celery
from app.tasks.email_templates import create_booking_confirmation_template
from config import config


@celery.task
def process_pic(path: str):
    im_path = Path(path)
    im = Image.open(im_path)
    im_resized = im.resize((1000, 500), Image.Resampling.BILINEAR)
    im_resized_mini = im.resize((200, 100), Image.Resampling.BILINEAR)
    im_resized.save(f"app/static/images/resized_1000_500_{im_path.name}")
    im_resized_mini.save(f"app/static/images/resized_200_100_{im_path.name}")


@celery.task
def send_booking_confirmation_email(booking: dict, email_to: EmailStr):
    print(f"{email_to=}")
    email_to_mock = config.SMTP_USER  # DELETE THIS PROD
    msg_content = create_booking_confirmation_template(booking, email_to_mock)
    print(f"{msg_content=}")

    with smtplib.SMTP_SSL(config.SMTP_HOST, config.SMTP_PORT) as server:
        server.login(config.SMTP_USER, config.SMTP_PASS)
        server.send_message(msg_content)
