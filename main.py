from contextlib import asynccontextmanager
from fastapi import FastAPI
from core.database import engine, Base

@asynccontextmanager
async def start_db(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

# Create FastAPI instance with the async db
app = FastAPI(lifespan=start_db)