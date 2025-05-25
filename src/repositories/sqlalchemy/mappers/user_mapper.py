from domain.entities.user import User
from repositories.sqlalchemy.models.user_model import UserModel

class UserMapper:
    @staticmethod
    def to_domain(model: UserModel) -> User:
        return User(name=model.name, email=model.email, password=model.password, transactions = model.transactions, goals=model.goals, id=model.id)

    @staticmethod
    def to_model(entity: User) -> UserModel:
        return UserModel(id=entity.id, name=entity.name, email=entity.email, password=entity.password)