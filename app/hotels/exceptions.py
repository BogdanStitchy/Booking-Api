from fastapi import HTTPException, status


class HotelsException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class IncorrectTimePeriodException(HotelsException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Срок выезда не может быть раньше срока въезда"


class IncorrectDurationTimeException(HotelsException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Срок бронирования не больше 100 дней"
