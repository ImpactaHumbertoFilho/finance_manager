from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from repositories.sqlalchemy.base import Base

class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(20), nullable=False)

    transactions = relationship("TransactionModel", back_populates="user", cascade="all, delete-orphan")
    goals = relationship("GoalModel", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<UserModel(id={self.id}, name='{self.name}', email='{self.email}')>"
