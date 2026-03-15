from datetime import date
from sqlalchemy import Date, ForeignKey, Integer, String
from core.database import Base
from sqlalchemy.orm import Mapped, mapped_column


class Portfolios(Base):
    __tablename__ = "portfolios"

    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    created_by:Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    date_added:Mapped[date] = mapped_column(Date, nullable=False)
    title:Mapped[str] = mapped_column(String(100), nullable=False)

class PortfolioFiles(Base):
    __tablename__ = "portfolio_files"

    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    portfolio_id:Mapped[int] = mapped_column(Integer, ForeignKey("portfolios.id"), nullable=False)
    file_name:Mapped[str] = mapped_column(String(255), nullable=False)
    file_path:Mapped[str] = mapped_column(String(255), nullable=False)
    date_added:Mapped[date] = mapped_column(Date, nullable=False)