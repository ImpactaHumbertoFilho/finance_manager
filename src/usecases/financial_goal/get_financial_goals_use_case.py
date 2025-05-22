from domain.repositories.financial_goal_repository_interface import IFinancialGoalRepository
from domain.usecases.financial_goal.get_financial_goals.get_financial_goals_use_case_interface import IGetFinancialGoalsUseCase

class GetFinancialGoalsUseCase(IGetFinancialGoalsUseCase):
    def __init__(self, financial_goals_repository: IFinancialGoalRepository):
        self.financial_goals_repository = financial_goals_repository

    def execute(self, user_id: str) -> list:
        return self.financial_goals_repository.get()