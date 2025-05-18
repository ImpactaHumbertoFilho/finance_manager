from domain.entities.user import User
from repositories.sqlalchemy.models.user_model import UserModel

class UserMapper:
    @staticmethod
    def to_domain(model: UserModel) -> User:
        return User(id=model.id, name=model.name, email=model.email)

    @staticmethod
    def to_model(entity: User) -> UserModel:
        return UserModel(id=entity.id, name=entity.name, email=entity.email)
