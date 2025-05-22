from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from repositories.sqlalchemy.base import Base

class TransactionModel(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Float, nullable=False)
    description = Column(String(255), nullable=True)
    date = Column(Date, nullable=False)
    type = Column(String(50), nullable=False)
    payment_method = Column(String(50), nullable=True)

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=True)

    user = relationship("UserModel", back_populates="transactions")
    category = relationship("CategoryModel", back_populates="transactions")
