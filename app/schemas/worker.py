from .user import UserBase


class WorkerBase(UserBase):
    cv: str | None = None
    skills: list[str] = []


class WorkerCreate(WorkerBase):
    password: str | None = None


class WorkerResponse(WorkerBase):
    id_worker: int
