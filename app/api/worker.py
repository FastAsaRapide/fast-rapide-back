from fastapi import APIRouter, Depends, status
from ..services import WorkderService
from ..schemas import (
    ApplicationCreate,
    ApplicationIncludeParentsResponse,
    WorkerCreate,
    WorkerResponse,
    WorkIncludePostResponse,
)
from typing import Annotated

router = APIRouter(prefix="/worker", tags=["Worker"])


@router.get("/", response_model=list[WorkIncludePostResponse])
async def list_workers(worker_service: Annotated[WorkderService, Depends()]):
    return worker_service.list_workers()


@router.post("/", response_model=WorkerResponse, status_code=status.HTTP_201_CREATED)
async def register(
    worker: WorkerCreate, worker_service: Annotated[WorkderService, Depends()]
):
    return await worker_service.register(worker)


@router.post(
    "/applied-post",
    response_model=ApplicationIncludeParentsResponse,
    status_code=status.HTTP_201_CREATED,
)
async def applied_to_post(
    application: ApplicationCreate, worker_service: Annotated[WorkderService, Depends()]
):
    return await worker_service.applied_post(application)
