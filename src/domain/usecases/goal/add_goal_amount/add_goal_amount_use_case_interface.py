from abc import ABC, abstractmethod

class IAddGoalAmountUseCase(ABC):
    @abstractmethod
    def execute(self, input_data):
        pass