from pydantic import BaseModel
from .worker import WorkerOut
from .post import PostOut


class ApplicationIn(BaseModel):
    worker_id: int
    post_id: int


class ApplicationOut(BaseModel):
    is_validated: bool
    worker: WorkerOut
    post: PostOut
