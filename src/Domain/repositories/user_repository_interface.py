from abc import ABC, abstractmethod
from typing import Optional
from domain.entities.user import User

class IUserRepository(ABC):
    @abstractmethod
    def add(self, user: User) -> User:
        pass
    
    @abstractmethod
    def update(self, id:int, user: User) -> User:
        pass
    
    @abstractmethod
    def delete(self, id:int) -> User:
        pass

    @abstractmethod
    def get(self) -> Optional[list[User]]:
        pass
    
    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[User]:
        pass
    
    @abstractmethod
    def get_by_email(self, email: str) -> Optional[User]:
        pass