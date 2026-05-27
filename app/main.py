from fastapi import FastAPI
from contextlib import asynccontextmanager
from .core import create_db_and_tables
from .api import recruiter, worker, post


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan, title="FASTASARAPIDE")


app.include_router(recruiter.router)
app.include_router(worker.router)
app.include_router(post.router)
