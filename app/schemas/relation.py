from .post import PostSimpleResponse
from .recruiter import RecruiterSimpleResponse
from typing import  Optional


class RecruiterResponse(RecruiterSimpleResponse):
    posts: list["PostSimpleResponse"]

class PostResponse(PostSimpleResponse):
    recruiter: Optional["RecruiterSimpleResponse"]
