from abc import ABC, abstractmethod

from domain.usecases.goal.update_goal.update_goal_input import UpdateGoalInput
from domain.usecases.goal.update_goal.update_goal_result import UpdateGoalResult


class IUpdateGoalUseCase(ABC):
    @abstractmethod
    def execute(self, updated_goal_input:UpdateGoalInput) -> UpdateGoalResult:
        pass