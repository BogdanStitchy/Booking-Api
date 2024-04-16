from pydantic import BaseModel


class SHotelsWithRoomsLeft(BaseModel):
    id: int
    name: str
    location: str
    services: list
    rooms_quantity: int
    image_id: int
    rooms_left: int


class SHotels(BaseModel):
    id: int
    name: str
    location: str
    services: list
    rooms_quantity: int
    image_id: int
