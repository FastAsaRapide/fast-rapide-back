from pydantic import BaseModel
from .worker import WorkerResponse


class PostBase(BaseModel):
    title: str | None = None
    context: str | None = None
    is_open: bool = True


class PostCreate(PostBase):
    recruiter_id: int


class PostSimpleResponse(PostBase):
    id_post: int


class PostIncludeWorkerResponse(PostSimpleResponse):
    workers: list["WorkerResponse"]
