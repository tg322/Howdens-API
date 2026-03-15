from datetime import date
from typing import List

from fastapi import UploadFile
from crud.portfolio import insert_portfolio, insert_portfolio_file
from crud.users import get_safe_user_by_email
from schemas.portfolio import NewPortfolioResponseData, PortfolioFile
from services.FileService import FileService
from sqlalchemy.ext.asyncio import AsyncSession

class PortfolioService:
    def __init__(self, db:AsyncSession, file_service:FileService):
        self.db = db
        self.file_service = file_service

    async def create_new_portfolio_with_files(self, email:str, portfolio_name:str, date_added:date, files:List[UploadFile]):
        # First, ensure email is valid, get safe user.
        get_safe_user_response = await get_safe_user_by_email(db=self.db, email=email)

        # If user does not exist, return error message.
        if get_safe_user_response is None:
            return {"error": "User does not exist"}
        
        # Now we insert the files after validating user
        upload_files_response = await self.file_service.store_files(base_path="portfolios", folder_name=portfolio_name, files=files)

        # Now we insert the portfolio into portfolios table
        insert_portfolio_response = await insert_portfolio(db=self.db, user=get_safe_user_response, date_added=date_added, title=portfolio_name)

        portfolio = insert_portfolio_response

        uploaded_portfolio_files:List[PortfolioFile] = []
        # Now we record the uploaded files to the portfolio_files table
        for uploaded_file in upload_files_response:
            insert_portfolio_file_response = await insert_portfolio_file(db=self.db, portfolio=portfolio, uploaded_file=uploaded_file)
            file_record = insert_portfolio_file_response
            # Stick file_record into uploaded files array
            uploaded_portfolio_files.append(file_record)
        
        response_data = NewPortfolioResponseData(portfolio=portfolio, portfolio_files=uploaded_portfolio_files)
        return {"message":"Portfolio successfully saved", "data":response_data}