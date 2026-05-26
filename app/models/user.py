from sqlmodel import  SQLModel


class User(SQLModel):
    phone: str 
    name: str
    first_name: str
    age: int = 18
    location: str
    password: str | None = None
    

