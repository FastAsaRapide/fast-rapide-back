from fastapi import APIRouter, Depends, status
from ..services import RecruiterService
from ..schemas import (
    RecruiterCreate,
    RecruiterResponse,
    PostCreate,
    PostResponse,
    ApplicationCreate,
    ApplicationResponse,
    PostIncludeWorkerResponse,
)
from typing import Annotated


router = APIRouter(prefix="/recruiter", tags=["Recruiter"])


# auth simplification for get the actual recruiter
def get_recruiter_id() -> int:
    return 1


@router.get("/", response_model=list[RecruiterResponse])
async def lists_recruiter(recruiter_service: Annotated[RecruiterService, Depends()]):
    return recruiter_service.lists_recruiter()


@router.get("/my-post", response_model=list[PostIncludeWorkerResponse])
async def all_post(
    id: int,
    recruiter_service: Annotated[RecruiterService, Depends()],
):
    return await recruiter_service.list_posts(id)


@router.post("/", response_model=RecruiterResponse, status_code=status.HTTP_201_CREATED)
async def register(
    recruiter: RecruiterCreate,
    recruiter_service: Annotated[RecruiterService, Depends()],
):
    return await recruiter_service.register(recruiter)


@router.post(
    "/create-post", response_model=PostResponse, status_code=status.HTTP_201_CREATED
)
async def create_post(
    post: PostCreate, recruiter_service: Annotated[RecruiterService, Depends()]
):
    return await recruiter_service.create_post(post)


@router.put("/validate-application", response_model=ApplicationResponse)
async def validate_application(
    application: ApplicationCreate,
    recruiter_service: Annotated[RecruiterService, Depends()],
):
    return await recruiter_service.validate_application(application)


@router.put("/close-post/{id}", response_model=PostIncludeWorkerResponse)
async def close_post(
    id: int,
    recruiter_service: Annotated[RecruiterService, Depends()],
    recruiter: Annotated[int, Depends(get_recruiter_id)],
):
    return await recruiter_service.close_post(recruiter, id)
