from contextlib import asynccontextmanager
from fastapi import FastAPI
from core.database import engine, Base
from models import users
from routes import authentication, portfolio
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def start_db(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

# Create FastAPI instance with the async db
app = FastAPI(lifespan=start_db)

origins = [
    "http://localhost:5173"  # your prod frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_headers=["*"],
    allow_methods=["*"]
)

app.include_router(authentication.router, prefix="/auth", tags=["Auth"])
app.include_router(portfolio.router, prefix='/portfolio', tags=["portfolio"])