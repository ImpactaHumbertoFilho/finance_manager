from abc import ABC, abstractmethod

class IGetFinancialGoalsUseCase(ABC):
    @abstractmethod
    def execute(self, user_id: str) -> list:
        """
        Retrieves a list of financial goals for the given user.

        :param user_id: The ID of the user whose financial goals are to be retrieved.
        :return: A list of financial goals associated with the user.
        """
        pass