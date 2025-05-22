from domain.entities.financial_goal import FinancialGoal
from domain.repositories.financial_goal_repository_interface import IFinancialGoalRepository
from domain.repositories.user_repository_interface import IUserRepository

from domain.usecases.financial_goal.create_financial_goal.create_financial_goal_input import CreateFinancialGoalInput
from domain.usecases.financial_goal.create_financial_goal.create_financial_goal_output import CreateFinancialGoalOutput
from domain.usecases.financial_goal.create_financial_goal.create_financial_goal_use_case import ICreateFinancialGoalUseCase

class CreateFinancialGoalUseCase(ICreateFinancialGoalUseCase):
    def __init__(self, financial_goal_repository: IFinancialGoalRepository, user_repository: IUserRepository):
        self.financial_goal_repository = financial_goal_repository
        self.user_repository = user_repository

    def execute(self, input_data: CreateFinancialGoalInput) -> CreateFinancialGoalOutput:
        user = self.user_repository.get_by_id(input_data.user_id)

        if user is None:
            raise ValueError("Usuário não encontrado.")

        if input_data.target_amount is None or not isinstance(input_data.target_amount, (int, float)) or input_data.target_amount <= 0:
            raise ValueError("A meta deve ser um número maior que 0.")

        financial_goal = FinancialGoal(
            user=user,
            name=input_data.name,
            target_amount=input_data.target_amount,
            current_amount=input_data.current_amount,
            deadline=input_data.deadline
        )

        result = self.financial_goal_repository.add(financial_goal)

        return CreateFinancialGoalOutput(
            id=result.id,
            user = result.user,
            name=result.name,
            target_amount=result.target_amount,
            current_amount=result.get_current_amount(),
            deadline=result.deadline
        )

