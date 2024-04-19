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
        f'Вы забронировали номер "{booking["room_name"]}"  в отеле <b>{booking["hotel_name"]}</b>.<br><br>'
        f"<b>Адрес</b>: с {booking['location']}<br>"
        f"<b>Даты бронирования</b>: с {booking['date_from']} по {booking['date_to']}<br>"
        f"<b>Итого дней проживания</b>: {booking['total_days']}<br>"
        f"<b>Итоговая стоимость к оплате</b>: {booking['total_cost']}<br><br><br>"
        f"С уважением, сервис по бронированию отелей.",
        subtype="html"
    )
    return email
