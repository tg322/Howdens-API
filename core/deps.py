from sqlalchemy.ext.asyncio import AsyncSession
from collections.abc import AsyncGenerator

from core.database import SessionLocal

# Create async db instance as a dependancy (Prevents circular imports, spawns a new instance per route)
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session