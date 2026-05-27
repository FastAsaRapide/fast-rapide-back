from ..dependencies import SessionDep
from ..repositories import CrudGen
from ..core import Recruiter
from ..schemas import RecruiterCreate, PostCreate, ApplicationCreate
from fastapi import status, HTTPException
from .post import PostService
from .application import ApplicationService


class RecruiterService:
    def __init__(self, session: SessionDep) -> None:
        self._repository = CrudGen(Recruiter, session)
        self._post_service = PostService(session)
        self._application_service = ApplicationService(session)

    async def register(self, data: RecruiterCreate) -> Recruiter:
        try:
            new_data = Recruiter(**data.model_dump())
            return self._repository.add(new_data)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    async def create_post(self, data: PostCreate):
        return await self._post_service.create_post(data)

    async def validate_application(self, data: ApplicationCreate):
        return await self._application_service.validate_application(data)

    async def close_post(self, recruiter_id: int, id: int):
        return await self._post_service.close_post(recruiter_id, id)

    async def list_posts(self, id: int):
        return await self._post_service.list_posts_by_recruiter(id)

    def lists_recruiter(self):
        return self._repository.find_all("id_recruiter")
