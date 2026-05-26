from sqlmodel import SQLModel, Field, Relationship
from typing import TYPE_CHECKING, Optional
from .application import Application


if TYPE_CHECKING:
    from .recruiter import Recruiter
    from .worker import Worker


class Post(SQLModel, table=True):
    id_post: int = Field(default=None, primary_key=True)
    title: str | None = None
    context: str | None = None
    is_open: bool = True
    recruiter_id: int = Field(foreign_key="recruiter.id_recruiter")
    recruiter: Optional["Recruiter"] = Relationship(back_populates="posts")
    workers: list["Worker"] = Relationship(
        back_populates="posts", link_model=Application
    )
