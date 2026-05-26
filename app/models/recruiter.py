from sqlmodel import Field, Relationship
from .user import User
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .post import Post


class Recruiter(User, table=True):
    id_recruiter: int = Field(default=None, primary_key=True)
    posts: list["Post"] = Relationship(back_populates="recruiter")
