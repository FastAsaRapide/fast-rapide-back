from .post import PostSimpleResponse
from .recruiter import RecruiterSimpleResponse
from typing import Optional
from .application import ApplicationResponse
from .worker import WorkerResponse, WorkBaseResponse


class RecruiterResponse(RecruiterSimpleResponse):
    posts: list["PostSimpleResponse"]


class PostResponse(PostSimpleResponse):
    recruiter: Optional["RecruiterSimpleResponse"]


class ApplicationIncludePostResponse(ApplicationResponse):
    post: PostResponse


class ApplicationIncludeWorkerResponse(ApplicationResponse):
    worker: WorkerResponse


class ApplicationIncludeParentsResponse(
    ApplicationIncludeWorkerResponse, ApplicationIncludePostResponse
): ...


class PostIncludeWorkerResponse(PostSimpleResponse):
    applications: list[ApplicationIncludeWorkerResponse]


class WorkIncludePostResponse(WorkBaseResponse):
    applications: list[ApplicationIncludeWorkerResponse]
