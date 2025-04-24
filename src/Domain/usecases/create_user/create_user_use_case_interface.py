from .create_user_input import CreateUserInput
from .create_user_result import CreateUserResult
from abc import ABC, abstractmethod

class ICreateUserUseCase(ABC):
    @abstractmethod
    def execute(self, input_data: CreateUserInput) -> CreateUserResult:
        pass
