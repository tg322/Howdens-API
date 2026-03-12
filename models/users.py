from sqlalchemy import ForeignKey, Integer, String
from core.database import Base
from sqlalchemy.orm import Mapped, mapped_column

class Users(Base):
    __tablename__ = "users"

    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    email:Mapped[str] = mapped_column(String(80), nullable=False, unique=True)
    password:Mapped[str] = mapped_column(String(255), nullable=False)

class UserDetails(Base):
    __tablename__ = "user_details"

    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id:Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    first_name:Mapped[str] = mapped_column(String(50), nullable=False)
    last_name:Mapped[str] = mapped_column(String(50), nullable=False)
    
