from ..dependencies import SessionDep
from ..repositories import CrudGen
from ..models import Recruiter
from ..schemas import RecruiterIn
from fastapi import status, HTTPException


class RecruiterService:
    async def __init__(self, session: SessionDep) -> None:
        self._repository = CrudGen(Recruiter, session)

    async def register(self, data: RecruiterIn) -> Recruiter:
        try:
            new_data = Recruiter(**data.model_dump())
            return self._repository.add(new_data)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    async def create_post(self): ...

    async def validate_application(self): ...

    async def close_post(self, id:int): ...
