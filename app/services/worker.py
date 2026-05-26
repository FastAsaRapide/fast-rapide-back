from ..dependencies import SessionDep
from ..repositories import CrudGen
from ..models import Worker
from ..schemas import WorkerIn, ApplicationIn
from fastapi import status, HTTPException
from .post import PostService
from .application import ApplicationService


class WorkderService:
    def __init__(self, session: SessionDep) -> None:
        self._repository = CrudGen(Worker, session)
        self._post_service = PostService(session)
        self._application_service = ApplicationService(session)

    async def register(self, data: WorkerIn) -> Worker:
        try:
            new_data = Worker(**data.model_dump())
            return self._repository.add(new_data)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    async def list_posts(self):
        return self._post_service.list_posts()

    async def applied_post(self, data: ApplicationIn):
        return self._application_service.applied_post(data)
