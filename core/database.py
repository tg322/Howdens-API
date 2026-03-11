from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

# aiosqlite is the async version of sqlite

DATABASE_URL = "sqlite+aiosqlite:///./app.db"

# Create database engine, allow multithread access (FastAPI compatability), create async version
engine = create_async_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Requires db.execute, db.commit, db.flush to be run intentionally rather than automatically. Create async session maker. This is the config for all spawned db instances.
SessionLocal = async_sessionmaker(
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
    bind=engine,
    expire_on_commit=False #Allows for refreshing inserted objects into db after commit.
)

# Base class that all DB models inherit from (Provides model visibility to database)

class Base(DeclarativeBase):
    pass