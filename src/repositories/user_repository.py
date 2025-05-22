from domain.repositories.user_repository_interface import IUserRepository
from repositories.sqlalchemy.mappers.user_mapper import UserMapper
from repositories.sqlalchemy.models.user_model import UserModel
from domain.entities.user import User

class UserRepository(IUserRepository):
    def __init__(self, session_factory):
        self.session_factory = session_factory

    def add(self, user: User) -> User:
        with self.session_factory() as session:
            model = UserMapper.to_model(user)
            session.add(model)
            session.commit()
            session.refresh(model)
            return UserMapper.to_domain(model)

    def update(self, id: int, user: User) -> User:
        with self.session_factory() as session:
            model = session.query(UserModel).filter_by(id=id).first()
            if model:
                model.name = user.name
                model.email = user.email
                session.commit()
                session.refresh(model)
                return UserMapper.to_domain(model)

    def delete(self, user_id: int) -> User:
        with self.session_factory() as session:
            model = session.query(UserModel).filter_by(id=user_id).first()
            if model:
                session.delete(model)
                session.commit()
                return UserMapper.to_domain(model)

    def get(self) -> list[User]:
        with self.session_factory() as session:
            models = session.query(UserModel).all()

            return [UserMapper.to_domain(model) for model in models]

    def get_by_id(self, user_id: int) -> User:
        with self.session_factory() as session:
            model = session.query(UserModel).filter_by(id=user_id).first()
            return UserMapper.to_domain(model) if model else None

    def get_by_email(self, email: str) -> User:
        with self.session_factory() as session:
            model = session.query(UserModel).filter_by(email=email).first()
            return UserMapper.to_domain(model) if model else None