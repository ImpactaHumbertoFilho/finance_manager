from .delete_user_result import DeleteUserResult
from .delete_user_input import DeleteUserInput
from abc import ABC, abstractmethod

class IDeleteUserUseCase(ABC):
    @abstractmethod
    def execute(self, input_data: DeleteUserInput) -> DeleteUserResult:
        pass
