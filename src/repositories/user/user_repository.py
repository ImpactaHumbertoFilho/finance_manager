from domain.repositories.user_repository_interface import IUserRepository
from domain.entities.user import User
from typing import Optional

class UserRepository(IUserRepository):
    def __init__(self):
        self.users = [
            User(name="Alice", email="alice@example.com", id=1),
            User(name="Bob", email="bob@example.com", id=2),
            User(name="Charlie", email="charlie@example.com", id=3),
            User(name="Diana", email="diana@example.com", id=4),
            User(name="Eve", email="eve@example.com", id=5),
            User(name="Frank", email="frank@example.com", id=6),
            User(name="Grace", email="grace@example.com", id=7),
            User(name="Hank", email="hank@example.com", id=8),
            User(name="Ivy", email="ivy@example.com", id=9),
            User(name="Jack", email="jack@example.com", id=10)
        ]
        
        self.next_id = 11

    def add(self, user: User) -> User:
        if user.id is None:
            user.id = self.next_id
            self.next_id += 1
        
        self.users.append(user)
        
        return user
 
    def update(self, user: User) -> Optional[User]:
        for i, existing_user in enumerate(self.users):
            if existing_user.id == user.id:
                
                self.users[i] = user
                return user
            
        return None

    def delete(self, user_id: int) -> bool:
        for i, user in enumerate(self.users):
            if user.id == user_id:
                del self.users[i]

                return True
        
        return False

    def get(self) -> list[User]:
        return self.users
    
    def get_by_id(self, user_id: int) -> Optional[User]:
        return next((user for user in self.users if user.id == user_id), None)

    def get_by_email(self, email: str) -> Optional[User]:
        return next((user for user in self.users if user.email == email), None)