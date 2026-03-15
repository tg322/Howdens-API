
from typing import List
from fastapi import APIRouter, File, Form, UploadFile


router = APIRouter()

@router.post("/upload_portfolio")
async def upload_portfolio(
    *,
    email: str = Form(...),
    portfolio_name: str = Form(...),
    files: List[UploadFile] = File(...)
):
    print(email)
    print(portfolio_name)
    print(files)