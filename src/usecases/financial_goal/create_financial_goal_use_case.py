from crosscutting.financial_goal_helper import FinancialGoalHelper
from domain.repositories.financial_goal_repository_interface import IFinancialGoalRepository
from domain.usecases.financial_goal.create_financial_goal.create_financial_goal_input import CreateFinancialGoalInput
from domain.usecases.financial_goal.create_financial_goal.create_financial_goal_output import CreateFinancialGoalOutput
from domain.usecases.financial_goal.create_financial_goal.create_financial_goal_use_case import ICreateFinancialGoalUseCase

class CreateFinancialGoalUseCase(ICreateFinancialGoalUseCase):
    def __init__(self, financial_goal_repository: IFinancialGoalRepository):
        self.financial_goal_repository = financial_goal_repository

    def execute(self, input_data: CreateFinancialGoalInput) -> CreateFinancialGoalOutput:
        financial_goal = FinancialGoalHelper.from_input(input_data)

        if financial_goal.target_amount is None or not isinstance(financial_goal.target_amount, (int, float)) or financial_goal.target_amount <= 0:
            raise ValueError("A meta deve ser um número maior que 0.")

        result = self.financial_goal_repository.add(financial_goal)

        return FinancialGoalHelper.to_output(result)

