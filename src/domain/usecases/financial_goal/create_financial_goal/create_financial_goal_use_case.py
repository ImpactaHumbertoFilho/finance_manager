from abc import ABC

from domain.usecases.financial_goal.create_financial_goal.create_financial_goal_input import CreateFinancialGoalInput
from domain.usecases.financial_goal.create_financial_goal.create_financial_goal_output import CreateFinancialGoalOutput

class ICreateFinancialGoalUseCase(ABC):
    """
    Interface for the CreateFinancialGoalUseCase.
    """

    def execute(self, input_data: CreateFinancialGoalInput) -> CreateFinancialGoalOutput:
        """
        Execute the use case to create a financial goal.

        :param input_data: The input data for creating a financial goal.
        :return: The output data after creating the financial goal.
        """
        pass