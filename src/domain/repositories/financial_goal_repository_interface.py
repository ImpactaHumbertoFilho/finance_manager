from typing import Optional
from domain.entities.financial_goal import FinancialGoal
from domain.usecases.financial_goal.create_financial_goal.create_financial_goal_output import CreateFinancialGoalOutput
from domain.usecases.financial_goal.create_financial_goal.create_financial_goal_input import CreateFinancialGoalInput
from abc import ABC, abstractmethod

class IFinancialGoalRepository(ABC):
    @abstractmethod
    def add(self, financial_goal: CreateFinancialGoalInput) -> CreateFinancialGoalOutput:
        pass
    
    @abstractmethod
    def update(self, financial_goal):
        pass
    
    @abstractmethod
    def delete(self, financial_goal_id):
        pass
    
    @abstractmethod
    def get(self, user_id: int) -> Optional[list[FinancialGoal]]:
        pass

    @abstractmethod
    def get_by_id(self, financial_goal_id):
        pass