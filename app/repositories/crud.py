from sqlmodel import Session, select, SQLModel
from typing import Type, Sequence
from uuid import UUID
from pydantic import BaseModel


ID = str | int | UUID


class CrudGen[T: SQLModel]:
    def __init__(self, model: Type[T], session: Session) -> None:
        self.model = model
        self.session = session

    def add(self, data: T) -> T:
        self.session.add(data)
        self.session.commit()
        self.session.refresh(data)
        return data

    def find_all(self, offset: int = 0, limit: int = 10) -> Sequence[T]:
        statement = select(self.model).offset(offset).limit(limit)
        return self.session.exec(statement).all()

    def get_one(self, id: ID) -> T:
        local_data = self.session.get(self.model, id)

        if not local_data:
            raise ValueError(f"No {self.model.__name__} found")

        return local_data

    def update(self, id: ID, data: BaseModel) -> T:
        local_data = self.get_one(id)
        local_data.sqlmodel_update(data.model_dump(exclude_unset=True))
        self.session.add(local_data)
        self.session.commit()
        self.session.refresh(local_data)

        return local_data

    def delete(self, id: ID) -> bool:

        local_data = self.get_one(id)
        self.session.delete(local_data)
        self.session.commit()
        return True

    def get_by_field(self, field: str, value):
        statement = select(self.model).where(getattr(self.model, field) == value)
        local_data = self.session.exec(statement).first()

        if not local_data:
            raise ValueError(f"{self.model.__name__} Not Found")

        return local_data
