from fastapi import APIRouter, Depends
from ..services import PostService
from ..schemas import PostIncludeWorkerResponse
from typing import Annotated

router = APIRouter(prefix="/post", tags=["Post"])


@router.get("/", response_model=list[PostIncludeWorkerResponse])
async def list_posts(post_service: Annotated[PostService, Depends()]):
    return await post_service.list_posts()
