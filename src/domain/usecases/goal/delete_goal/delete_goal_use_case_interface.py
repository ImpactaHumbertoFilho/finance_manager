from abc import ABC, abstractmethod

class IDeleteGoalUseCase(ABC):
    @abstractmethod
    def execute(self, goal_id: str) -> None:
        pass