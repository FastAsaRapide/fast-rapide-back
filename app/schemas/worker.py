from .user import UserBase
from pydantic import BaseModel


class WorkerBase(UserBase):
    cv: str | None = None
    skills: list[str] = []


class WorkerCreate(WorkerBase):
    password: str | None = None


class WorkBaseResponse(BaseModel):
    id_worker: int


class WorkerResponse(WorkerBase, WorkBaseResponse): ...
