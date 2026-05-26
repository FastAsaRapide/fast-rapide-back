from sqlmodel import Field, Column, JSON, Relationship
from typing import TYPE_CHECKING
from .user import User
from .application import Application

if TYPE_CHECKING:
    from .post import Post


class Worker(User, table=True):
    id_worker: int = Field(default=None, primary_key=True)
    cv: str | None = None
    skills: list[str] = Field(sa_column=Column(JSON), default=[])
    posts: list["Post"] = Relationship(back_populates="workers", link_model=Application)
