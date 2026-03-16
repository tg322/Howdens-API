from datetime import date
from typing import List
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from models.portfolios import PortfolioFiles, Portfolios
from models.users import UserDetails, Users
from schemas.files import UploadedFile
from schemas.portfolio import Portfolio, PortfolioFile, PortfolioItem
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

async def get_table_portfolios(db:AsyncSession):

    # id:int Porfolio.id
    # created_by_email:str User.email
    # created_by_first_name:str UserDetails.first_name
    # created_by_last_name:str UserDetails.last_name
    # date_added:date   Portfolio.date_added
    # title:str Portfolio.title

    try:

        stmt = (
            select(
                Portfolios.id, 
                Users.email.label("created_by_email"), 
                UserDetails.first_name.label("created_by_first_name"), 
                UserDetails.last_name.label("created_by_last_name"),
                Portfolios.date_added,
                Portfolios.title,
                func.count(PortfolioFiles.id).label("total_files")
            )
            .outerjoin(Users, Users.id == Portfolios.created_by)
            .join(UserDetails, UserDetails.user_id == Users.id)
            .outerjoin(PortfolioFiles, PortfolioFiles.portfolio_id == Portfolios.id)
            .group_by(
                Portfolios.id,
                Portfolios.title
            )
        )

        result = await db.execute(stmt)

    except SQLAlchemyError as exc:
        raise exc
    
    rows = result.mappings().all()

    return [PortfolioItem.model_validate(r) for r in rows]