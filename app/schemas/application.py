from pydantic import BaseModel
from datetime import datetime

class ApplicationCreate(BaseModel):
    worker_id: int
    post_id: int


class ApplicationResponse(BaseModel):
    is_validated: bool
    applied_at: datetime


