from datetime import date
from typing import List
from fastapi import APIRouter, Depends, File, Form, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from core.deps import get_db
from crud.portfolio import get_table_portfolios, insert_portfolio, insert_portfolio_file
from crud.users import get_safe_user_by_email
from schemas.portfolio import NewPortfolioResponseData, PortfolioFile
from services.PortfolioService import PortfolioService
from services.FileService import FileService


router = APIRouter()

@router.post("/upload_portfolio")
async def upload_portfolio(
    *,
    email: str = Form(...),
    portfolio_name: str = Form(...),
    date_added:date = Form(...),
    files: List[UploadFile] = File(...),
    db:AsyncSession = Depends(get_db)
):

    file_service = FileService()

    portfolio_service = PortfolioService(db=db, file_service=FileService())

    create_new_portfolio_with_files_response = await portfolio_service.create_new_portfolio_with_files(email=email, portfolio_name=portfolio_name, date_added=date_added, files=files)

    return create_new_portfolio_with_files_response

@router.get("/get_all_portfolios")
async def get_all_portfolios(
    *,
    db:AsyncSession = Depends(get_db)
):
    response = await get_table_portfolios(db=db)

    return response