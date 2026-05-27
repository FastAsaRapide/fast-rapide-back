from fastapi import APIRouter, Depends, status
from ..services import RecruiterService
from ..schemas import RecruiterCreate, RecruiterResponse
from typing import Annotated


router = APIRouter(prefix="/recruiter", tags=["Recruiter"])


@router.post("/", response_model=RecruiterResponse, status_code=status.HTTP_201_CREATED)
async def register(
    recruiter: RecruiterCreate,
    recruiter_service: Annotated[RecruiterService, Depends()],
):
    return await recruiter_service.register(recruiter)
    ...
