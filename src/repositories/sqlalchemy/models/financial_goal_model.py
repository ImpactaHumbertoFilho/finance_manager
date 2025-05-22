from sqlalchemy import Column, ForeignKey, Integer, String
from repositories.sqlalchemy.base import Base
from sqlalchemy.orm import relationship

class FinancialGoalModel(Base):
    __tablename__ = 'financial_goals'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    target_amount = Column(Integer, nullable=False)
    current_amount = Column(Integer, nullable=False)
    deadline = Column(String(10), nullable=False)

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("UserModel", back_populates="goals")
    
    def __repr__(self):
        return f"<FinancialGoalModel(id={self.id}, name='{self.name}', target_amount={self.target_amount}, current_amount={self.current_amount}, deadline='{self.deadline}', user_id={self.user_id})>"