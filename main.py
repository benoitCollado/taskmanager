from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import init_db
from routers import task

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(task.router)