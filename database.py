from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from contextlib import asynccontextmanager
from typing import AsyncGenerator

DATABASE_URL = "sqlite+aiosqlite:///./test.db"

engine = create_async_engine(DATABASE_URL, echo=True)

async_session_local = async_sessionmaker(bind=engine, expire_on_commit=False)

Base = declarative_base()

async def init_db():
  async with engine.begin() as conn:
    await conn.run_sync(Base.metadata.create_all)


async def get_db() -> AsyncGenerator[AsyncSession, None] :
  async with async_session_local() as session:
    yield session