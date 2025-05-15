
from abc import ABC, abstractmethod

from domain.usecases.update_user.update_user_input import UpdateUserInput
from domain.usecases.update_user.update_user_result import UpdateUserResult

class IUpdateUserUseCase(ABC):
    @abstractmethod
    def execute(self, input: UpdateUserInput) -> UpdateUserResult:
        pass