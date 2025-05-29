from abc import ABC, abstractmethod

class ICreateTransactionUseCase(ABC):
    @abstractmethod
    def execute(self, transaction_data):
        pass