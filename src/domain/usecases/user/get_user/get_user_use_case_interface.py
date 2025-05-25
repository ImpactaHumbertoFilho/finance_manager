from domain.usecases.user.get_user.get_user_result import GetUserResult
from abc import ABC, abstractmethod

class IGetUserUseCase(ABC):
    @abstractmethod
    def execute(self) -> dict[GetUserResult]:
        """
        Retrieves all users from the database.

        :return: A dictionary containing information of all users.
        """
        pass;