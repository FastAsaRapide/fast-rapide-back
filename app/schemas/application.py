from pydantic import BaseModel
from .worker import WorkerResponse
from .relation import PostResponse


class ApplicationCreate(BaseModel):
    worker_id: int
    post_id: int


class ApplicationResponse(BaseModel):
    is_validated: bool
    worker: WorkerResponse
    post: PostResponse
