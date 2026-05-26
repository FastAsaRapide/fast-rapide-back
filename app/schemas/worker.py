from .user import UserBase
from .post import PostOut


class WorkerBase(UserBase):
    cv: str | None = None
    skills: list[str] = []


class WorkerIn(WorkerBase):
    password: str | None = None


class WorkerOut(WorkerBase):
    id_worker: int
    posts: list[PostOut]
