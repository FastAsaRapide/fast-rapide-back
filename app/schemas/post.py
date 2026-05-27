from pydantic import BaseModel

class PostBase(BaseModel):
    title: str | None = None
    context: str | None = None
    is_open: bool = True


class PostCreate(PostBase):
    recruiter_id: int


class PostSimpleResponse(PostBase):
    id_post: int


