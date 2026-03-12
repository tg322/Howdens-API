from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError

from models.users import Users

async def get_user_password_hash_by_email(db:AsyncSession, email:str) -> str | None:
    # Select user password hash where user email == provided email
    # Return only one item, otherwise return None (error occured with unique email)
    try:
        stmt = (
            select(Users.password)
            .where(Users.email == email)
        )

        result = await db.execute(stmt)

    except SQLAlchemyError as exc:
        raise exc
    
    row = result.scalars().one_or_none()

    return row