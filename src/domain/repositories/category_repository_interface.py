from abc import ABC, abstractmethod
from domain.repositories.base_repository_interface import IBaseRepository

class ICategoryRepository(IBaseRepository):
    @abstractmethod
    def get_by_transaction(self, transaction_id):
        pass

