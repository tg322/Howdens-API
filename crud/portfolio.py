from datetime import date
from sqlalchemy.ext.asyncio import AsyncSession
from models.portfolios import PortfolioFiles, Portfolios
from schemas.files import UploadedFile
from schemas.portfolio import Portfolio, PortfolioFile
from schemas.users import SafeUser
from sqlalchemy.exc import SQLAlchemyError


async def insert_portfolio(db:AsyncSession, user:SafeUser, date_added:date, title:str) -> Portfolio:
    try:
        obj = Portfolios(
            created_by = user.id,
            date_added = date_added,
            title = title
        )

        db.add(obj)
        await db.flush()
        await db.commit()
        await db.refresh(obj)
    except SQLAlchemyError as exc:
        raise exc
    
    return Portfolio.model_validate(obj, from_attributes=True)

async def insert_portfolio_file(db:AsyncSession, portfolio:Portfolio, uploaded_file:UploadedFile) -> PortfolioFile:
    try:
        obj = PortfolioFiles(
            portfolio_id = portfolio.id,
            file_name = uploaded_file.file_name,
            file_path = uploaded_file.file_path,
            date_added = portfolio.date_added
        )

        db.add(obj)
        await db.flush()
        await db.commit()
        await db.refresh(obj)
    except SQLAlchemyError as exc:
        raise exc
    
    return PortfolioFile.model_validate(obj, from_attributes=True)