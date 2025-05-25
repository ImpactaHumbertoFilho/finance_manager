from domain.entities.financial_goal import FinancialGoal
from domain.repositories.financial_goal_repository_interface import IFinancialGoalRepository
from repositories.sqlalchemy.base import SessionLocal
from sqlalchemy.orm import Session

from repositories.sqlalchemy.mappers.financial_goal_mapper import FinancialGoalMapper
from repositories.sqlalchemy.models.financial_goal_model import FinancialGoalModel

class FinancialGoalRepository(IFinancialGoalRepository):
    def __init__(self, session_factory):
        self.session_factory = session_factory

    def add(self, financial_goal):
        with self.session_factory() as session:
            model = FinancialGoalMapper.to_model(financial_goal)  # CONVERTE para modelo SQLAlchemy
            session.add(model)
            session.commit()
            session.refresh(model)
        
            return FinancialGoalMapper.to_domain(model)
    
    def update(self, financial_goal):
        with self.session_factory() as session:
            session.commit()
            session.refresh(financial_goal)

            return financial_goal
    
    def delete(self, financial_goal_id):
        with self.session_factory() as session:
            financial_goal = session.query(FinancialGoalModel).filter(FinancialGoalModel.id == financial_goal_id).first()
            
            if financial_goal:
                session.delete(financial_goal)
                session.commit()
                return True
            
            return False
    
    def get(self, user_id):
        with self.session_factory() as session:
            financial_goals: list[FinancialGoalModel] = session.query(FinancialGoalModel).filter(FinancialGoalModel.user_id == user_id).all()
            
            return [FinancialGoal(goal.name, goal.user, goal.deadline, goal.target_amount, goal.current_amount, goal.id ) for goal in financial_goals]

    def get_by_id(self, financial_goal_id):
        with self.session_factory() as session:
            financial_goal = session.query(FinancialGoalModel).filter(FinancialGoalModel.id == financial_goal_id).first()
            
            return financial_goal