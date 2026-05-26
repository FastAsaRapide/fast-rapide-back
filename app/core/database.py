from sqlmodel import create_engine, SQLModel, Session
from .config import config
from ..models import *

engine = create_engine(config.DATABASE_URL)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    print("created......")


def get_session():
    with Session(engine) as session:
        yield session
