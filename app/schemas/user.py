from pydantic import BaseModel, Field


class User(BaseModel):
    phone: str = Field(min_length=14)
    name: str
    first_name: str
    age: int = 18
    location: str | None = None
    password: str | None = None
