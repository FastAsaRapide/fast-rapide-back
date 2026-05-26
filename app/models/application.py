from sqlmodel import SQLModel, Field
from datetime import datetime


class Application(SQLModel, table=True):
    worker_id: int = Field(foreign_key="worker.id_worker", primary_key=True)
    post_id: int = Field(foreign_key="post.id_post", primary_key=True)
    is_validated: bool = False
    applied_at: datetime = Field(default_factory=datetime.now)
