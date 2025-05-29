from abc import ABC, abstractmethod

from domain.repositories.base_repository_interface import IBaseRepository

class ITransactionRepository(IBaseRepository, ABC):
    @abstractmethod
    def get_by_id(self, transaction_id):
        pass

    @abstractmethod
    def get_by_user_id(self, user_id):
        pass

    @abstractmethod
    def get_by_category(self, category_id):
        pass

    @abstractmethod
    def get_by_payment_method(self, payment_method_id):
        pass