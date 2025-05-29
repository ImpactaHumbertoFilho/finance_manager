from abc import ABC, abstractmethod

class IBaseRepository(ABC):
    @abstractmethod
    def add(self, data):
        pass

    @abstractmethod
    def update(self, data):
        pass

    @abstractmethod
    def delete(self, id: int):
        pass

    @abstractmethod
    def get_by_id(self, id: int):
        pass

    @abstractmethod
    def get(self):
        pass
