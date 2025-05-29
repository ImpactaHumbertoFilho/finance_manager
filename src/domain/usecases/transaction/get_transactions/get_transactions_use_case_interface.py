from abc import ABC, abstractmethod

class IGetTransactionsUseCase(ABC):
    @abstractmethod
    def execute(self, user_id: int):
        pass