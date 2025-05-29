from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from repositories.sqlalchemy.base import Base

class PaymentMethodModel(Base):
    __tablename__ = 'payment_methods'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)
    
    transactions = relationship("TransactionModel", back_populates="payment_method", cascade="all, delete-orphan")