from sqlalchemy.ext.asyncio import AsyncSession

class AuthService:
    def __init__(self, db:AsyncSession):
        print()