from datetime import date
from typing import List
from pydantic import BaseModel


class PortfolioItem(BaseModel):
    id:int
    created_by_email:str
    created_by_first_name:str
    created_by_last_name:str
    date_added:date
    title:str
    total_files:int

class Portfolio(BaseModel):
    id:int
    created_by:int
    date_added:date
    title:str

class PortfolioFile(BaseModel):
    id:int
    portfolio_id:int
    file_name:str
    file_path:str
    date_added:date

class NewPortfolioResponseData(BaseModel):
    portfolio:Portfolio
    portfolio_files:List[PortfolioFile]
