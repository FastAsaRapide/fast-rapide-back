from fastapi import APIRouter, Depends
from ..services import RecruiterService
from ..schemas import RecruiterIn, RecruiterOut
from typing import Annotated


router = APIRouter(prefix="/recruiter", tags=["Recruiter"])


@router.post("/", response_model=RecruiterOut)
async def register(
    recruiter: RecruiterIn, recruiter_service: Annotated[RecruiterService, Depends()]
):
    return recruiter_service.register(recruiter)
    ...
