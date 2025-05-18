from sqlalchemy.orm import Session
from repositories.sqlalchemy.base import SessionLocal
from domain.repositories.user_repository_interface import IUserRepository
from domain.entities.user import User
from repositories.sqlalchemy.models.user_model import UserModel
from repositories.sqlalchemy.mappers.user_mapper import UserMapper

class UserRepository(IUserRepository):
    def __init__(self):
        self.session: Session = SessionLocal()

    def add(self, user: User) -> User:
        model = UserMapper.to_model(user)
        self.session.add(model)
        self.session.commit()
        self.session.refresh(model)
        return UserMapper.to_domain(model)

    def get_by_email(self, email: str) -> User:
        model = self.session.query(UserModel).filter_by(email=email).first()
        return UserMapper.to_domain(model) if model else None

    def get_by_id(self, user_id: int) -> User:
        model = self.session.query(UserModel).filter_by(id=user_id).first()
        return UserMapper.to_domain(model) if model else None

    def get(self) -> list[User]:
        models = self.session.query(UserModel).all()
        return [UserMapper.to_domain(model) for model in models]

    def delete(self, user_id: int) -> User:
        model = self.session.query(UserModel).filter_by(id=user_id).first()
        if model:
            self.session.delete(model)
            self.session.commit()
            return UserMapper.to_domain(model)

    def update(self, id: int, user: User) -> User:
        model = self.session.query(UserModel).filter_by(id=id).first()
        if model:
            model.name = user.name
            model.email = user.email
            self.session.commit()
            self.session.refresh(model)
            return UserMapper.to_domain(model)
