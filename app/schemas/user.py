from pydantic import BaseModel, Field


class UserBase(BaseModel):
    phone: str = Field(min_length=14)
    name: str
    first_name: str
    age: int = 18
    location: str | None = None
