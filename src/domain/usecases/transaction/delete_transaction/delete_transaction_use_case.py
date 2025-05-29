from abc import ABC, abstractmethod

class IDeleteTransactionUseCase(ABC):
    @abstractmethod
    def execute(self, transaction_id):
        pass