from pydantic import BaseModel
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .recruiter import RecruiterOut
    from .worker import WorkerOut


class PostIn(BaseModel):
    title: str | None = None
    context: str | None = None
    is_open: bool = True
    recruiter_id: int


class PostOut(PostIn):
    id_post: int
    recruiter: Optional["RecruiterOut"]
    workers: list["WorkerOut"]

