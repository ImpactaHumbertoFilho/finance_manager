# usecases/implementations/create_user_use_case.py

from domain.usecases.create_user.create_user_input import CreateUserInput
from domain.usecases.create_user.create_user_result import CreateUserResult
from domain.usecases.create_user.create_user_use_case_interface import ICreateUserUseCase

from domain.entities.user import User
from domain.repositories.user_repository_interface import IUserRepository


class CreateUserUseCase(ICreateUserUseCase):
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def execute(self, input_data: CreateUserInput) -> CreateUserResult:
        user = User(name=input_data.name, email=input_data.email)

        db_user = self.user_repository.add(user)

        return CreateUserResult(
            user_id=db_user.id,
            name=db_user.name,
            email=db_user.email
        )
