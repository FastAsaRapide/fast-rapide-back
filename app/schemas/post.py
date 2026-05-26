from pydantic import BaseModel
from .recruiter import RecruiterOut
from .worker import WorkerOut


class PostIn(BaseModel):
    title: str | None = None
    context: str | None = None
    is_open: bool = True
    recruiter_id: int


class PostOut(PostIn):
    id_post: int
    recruiter: RecruiterOut
    workers: list[WorkerOut]
