from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession

from core.deps import get_db
from core.security import HashPassword
from crud.authentication import get_user_password_hash_by_email
from crud.users import get_user_account_details_by_email
from schemas.authentication import LoginPayload
from services.authentication import AuthService

router = APIRouter()

@router.post("/hash_password")
async def return_hash(
    *,
    payload:LoginPayload,
):
    password_hasher = HashPassword()
    hashed_provided_password = password_hasher.hash_password(password=payload.password)

    return hashed_provided_password


@router.post("/login")
async def login(
    *,
    payload:LoginPayload,
    response:Response,
    db:AsyncSession = Depends(get_db)
):

    auth_service = AuthService(db=db, password_hasher=HashPassword())

    auth_response = await auth_service.login(payload=payload)

    return auth_response
