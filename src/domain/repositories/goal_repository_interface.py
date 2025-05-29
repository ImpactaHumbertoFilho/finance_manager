from typing import Optional
from domain.entities.goal import Goal
from domain.usecases.goal.create_goal.create_goal_output import CreateGoalOutput
from domain.usecases.goal.create_goal.create_goal_input import CreateGoalInput
from abc import ABC, abstractmethod

class IGoalRepository(ABC):
    @abstractmethod
    def add(self, goal: CreateGoalInput):
        pass
    
    @abstractmethod
    def update(self, goal):
        pass
    
    @abstractmethod
    def delete(self, goal_id):
        pass
    
    @abstractmethod
    def get(self, user_id: int) -> Optional[list[Goal]]:
        pass

    @abstractmethod
    def get_by_id(self, goal_id):
        pass
    
    @abstractmethod
    def get_by_user_id(self, user_id):
        pass