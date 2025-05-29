from domain.repositories.base_repository_interface import IBaseRepository
from abc import ABC, abstractmethod

class IPaymentMethodRepository(IBaseRepository):
    @abstractmethod
    def get_by_transaction_id(self, transaction_id):
        pass