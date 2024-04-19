from email.message import EmailMessage
from config import config
from pydantic import EmailStr


def create_booking_confirmation_template(booking: dict, email_to: EmailStr):
    email = EmailMessage()

    email["Subject"] = "Подтверждение бронирования"
    email["From"] = config.SMTP_USER
    email["To"] = email_to
    email.set_content(
        f"<h1>Подтвердите бронирование</h1>\n"
        f"Вы забронировали отель _Название отеля_ с {booking['date_from']} "
        f"по {booking['date_to']}",
        subtype="html"
    )
    return email
