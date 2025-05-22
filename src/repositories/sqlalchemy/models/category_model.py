from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from repositories.sqlalchemy.base import Base

class CategoryModel(Base):  # Corrija aqui
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)

    transactions = relationship("TransactionModel", back_populates="category", cascade="all, delete-orphan")