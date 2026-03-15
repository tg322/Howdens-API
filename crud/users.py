from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError

from models.users import UserDetails, Users
from schemas.users import SafeUser, UsersDetails

async def get_user_account_details_by_email(db:AsyncSession, email:str) -> UsersDetails | None:
    try:
        stmt = (
            select(Users.email.label("email"), UserDetails.first_name, UserDetails.last_name)
            .outerjoin(UserDetails, UserDetails.user_id == Users.id)
            .where(Users.email == email)
        )

        result = await db.execute(stmt)
    except SQLAlchemyError as exc:
        raise exc
    
    row = result.mappings().one_or_none()

    if row is None:
        return row

    return UsersDetails.model_validate(row)

async def get_safe_user_by_email(db:AsyncSession, email:str) -> SafeUser | None:
    try:
        stmt = (
            select(Users.id, Users.email)
            .where(Users.email == email)
        )

        result = await db.execute(stmt)

    except SQLAlchemyError as exc:
        raise exc
    
    row = result.mappings().one_or_none()

    if row is None:
        return None
    
    return SafeUser.model_validate(row)