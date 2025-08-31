from sqlalchemy import Integer, String, Boolean
from database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, ForeignKey
from typing import List
from database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Blog(Base):
    __tablename__ = 'blog'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
    publisher: Mapped[str] = mapped_column(String, nullable=False)
    category: Mapped[str] = mapped_column(String, nullable=False)
    time: Mapped[str] = mapped_column(String, nullable=False)
    isPublished: Mapped[bool] = mapped_column(Boolean, default=True)
    price: Mapped[int] = mapped_column(Integer, default=200)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), index=True)
    
    creator: Mapped["User"] = relationship(back_populates="blogs")
    
    
class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)
    
    blogs: Mapped[List["Blog"]] = relationship(back_populates="creator")
    