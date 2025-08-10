from sqlalchemy import Integer, String, Boolean
from database import Base
from sqlalchemy.orm import Mapped, mapped_column

class Blog(Base):
    __tablename__ = 'blog'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
    publisher: Mapped[str] = mapped_column(String, nullable=False)
    category: Mapped[str] = mapped_column(String, nullable=False)
    time: Mapped[str] = mapped_column(String, nullable=False)  # or DateTime if you prefer
    isPublished: Mapped[bool] = mapped_column(Boolean, default=True)
    price: Mapped[int] = mapped_column(Integer, default=200)