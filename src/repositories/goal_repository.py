from domain.entities.goal import Goal
from domain.repositories.goal_repository_interface import IGoalRepository
from repositories.sqlalchemy.base import SessionLocal
from sqlalchemy.orm import Session

from repositories.sqlalchemy.mappers.goal_mapper import GoalMapper
from repositories.sqlalchemy.models.goal_model import GoalModel

class GoalRepository(IGoalRepository):
    def __init__(self, session_factory):
        self.session_factory = session_factory

    def add(self, goal):
        with self.session_factory() as session:
            model = GoalMapper.to_model(goal)
            session.add(model)
            session.commit()
            session.refresh(model)
        
            return GoalMapper.to_domain(model)
    
    def update(self, goal):
        with self.session_factory() as session:
            model = session.query(GoalModel).filter(GoalModel.id == goal.id).first()
            if not model:
                return None
            
            model.name = goal.name
            model.user_id = goal.user_id
            model.deadline = goal.deadline
            model.target_amount = goal.target_amount
            model.current_amount = goal.current_amount

            session.commit()
            session.refresh(model)
            return GoalMapper.to_domain(model)
    
    def delete(self, goal_id):
        with self.session_factory() as session:
            goal = session.query(GoalModel).filter(GoalModel.id == goal_id).first()
            
            if goal:
                session.delete(goal)
                session.commit()
                return True
            
            return False
    
    def get(self, user_id):
        with self.session_factory() as session:
            goals: list[GoalModel] = session.query(GoalModel).filter(GoalModel.user_id == user_id).all()
            
            return [Goal(goal.name, goal.user, goal.deadline, goal.target_amount, goal.current_amount, goal.id ) for goal in goals]

    def get_by_id(self, goal_id):
        with self.session_factory() as session:
            goal = session.query(GoalModel).filter(GoalModel.id == goal_id).first()
            
            return GoalMapper.to_domain(goal)
        
    def get_by_user_id(self, user_id):
        with self.session_factory() as session:
            goals = session.query(GoalModel).filter(GoalModel.user_id == user_id).all()
            
            return [GoalMapper.to_domain(goal) for goal in goals] if goals else []