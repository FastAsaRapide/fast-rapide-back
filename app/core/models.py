from sqlmodel import SQLModel, Field, Relationship, Column, JSON
from typing import Optional
from datetime import datetime


class User(SQLModel):
    phone: str
    name: str
    first_name: str
    age: int = 18
    location: str
    password: str | None = None


class Recruiter(User, table=True):
    id_recruiter: int = Field(default=None, primary_key=True)
    posts: list["Post"] = Relationship(back_populates="recruiter")


class Application(SQLModel, table=True):
    worker_id: int = Field(foreign_key="worker.id_worker", primary_key=True)
    post_id: int = Field(foreign_key="post.id_post", primary_key=True)
    is_validated: bool = False
    applied_at: datetime = Field(default_factory=datetime.now)
    post: Optional["Post"] = Relationship(back_populates="applications")
    worker: Optional["Worker"] = Relationship(back_populates="applications")


class Worker(User, table=True):
    id_worker: int = Field(default=None, primary_key=True)
    cv: str | None = None
    skills: list[str] = Field(sa_column=Column(JSON), default=[])
    # posts: list["Post"] = Relationship(back_populates="workers", link_model=Application)
    applications: list["Application"] = Relationship(back_populates="worker")


class Post(SQLModel, table=True):
    id_post: int = Field(default=None, primary_key=True)
    title: str | None = None
    context: str | None = None
    is_open: bool = True
    recruiter_id: int = Field(foreign_key="recruiter.id_recruiter")
    recruiter: Optional["Recruiter"] = Relationship(back_populates="posts")
    # workers: list["Worker"] = Relationship(
    #     back_populates="posts", link_model=Application
    # )
    applications: list["Application"] = Relationship(back_populates="post")
