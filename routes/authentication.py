from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession

from core.deps import get_db
from core.security import HashPassword
from crud.authentication import get_user_password_hash_by_email
from crud.users import get_user_account_details_by_email
from schemas.authentication import LoginPayload

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
    password_hasher = HashPassword()

    # Get hash from db
    stored_hash = await get_user_password_hash_by_email(db=db, email=payload.email)
    if stored_hash is None:
        return {"error": "Account does not exist."}
    # Send provided_password and stored hash to password_hasher
    password_check_result = password_hasher.validate_password(provided_password=payload.password, stored_hash=stored_hash)
    # if false, send error message, if true, send back user details
    if password_check_result is False:
        return {"error": "Password was incorrect."}
    
    user_details_response = await get_user_account_details_by_email(db=db, email=payload.email)

    if user_details_response is None:
        return {"error": "An error occurred when fetching your account"}
    
    return user_details_response
