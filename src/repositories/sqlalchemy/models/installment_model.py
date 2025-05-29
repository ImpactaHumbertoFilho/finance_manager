from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from repositories.sqlalchemy.base import Base

class InstallmentModel(Base):
    __tablename__ = 'installments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(Integer, nullable=False)
    amount = Column(Float, nullable=False)
    due_date = Column(String(12), nullable=False)
    
    transaction_id = Column(Integer, ForeignKey('transactions.id'), nullable=False)

    transaction = relationship("TransactionModel", back_populates="installments")

    def __repr__(self):
        return f"<InstallmentModel(number={self.number}, amount={self.amount}, due_date={self.due_date})>"