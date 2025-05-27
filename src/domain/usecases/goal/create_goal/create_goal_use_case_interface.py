from abc import ABC

from domain.usecases.goal.create_goal.create_goal_input import CreateGoalInput
from domain.usecases.goal.create_goal.create_goal_output import CreateGoalOutput

class ICreateGoalUseCase(ABC):
    """
    Interface for the CreateGoalUseCase.
    """

    def execute(self, input_data: CreateGoalInput) -> CreateGoalOutput:
        """
        Execute the use case to create a financial goal.

        :param input_data: The input data for creating a financial goal.
        :return: The output data after creating the financial goal.
        """
        pass