from abc import ABC, abstractmethod

class IUpdateTransactionUseCase(ABC):
    @abstractmethod
    def execute(self, transaction_id):
        pass