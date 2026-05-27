from .user import UserBase


class RecruiterCreate(UserBase):
    password: str | None = None


class RecruiterSimpleResponse(UserBase):
    id_recruiter: int
