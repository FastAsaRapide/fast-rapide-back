from ..dependencies import SessionDep
from ..repositories import CrudGen
from ..core import Application
from ..schemas import ApplicationCreate
from fastapi import status, HTTPException
from sqlmodel import select


class ApplicationService:
    def __init__(self, session: SessionDep) -> None:
        self._repository = CrudGen(Application, session)

    async def applied_post(self, data: ApplicationCreate) -> Application:
        try:
            new_data = Application(**data.model_dump())
            return self._repository.add(new_data)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    async def validate_application(self, data: ApplicationCreate) -> Application:
        statement = select(Application).where(
            Application.post_id == data.post_id,
            Application.worker_id == data.worker_id,
        )
        session = self._repository.session

        application = session.exec(statement).first()

        print(data, application, sep="\n")

        if not application:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Job Applied not found"
            )

        application.is_validated = True
        session.add(application)
        session.commit()
        session.refresh(application)
        return application
