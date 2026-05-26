from .user import UserBase
from .post import PostOut
class RecruiterIn(UserBase):
    password: str | None = None


class RecruiterOut(UserBase):
    id_recruiter: int
    posts: list[PostOut]
