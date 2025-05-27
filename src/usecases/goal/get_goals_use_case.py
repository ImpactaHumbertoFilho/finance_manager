from domain.repositories.goal_repository_interface import IGoalRepository
from domain.usecases.goal.get_goals.get_goals_output import GetGoalsOutput, GetGoalsOutputItem
from domain.usecases.goal.get_goals.get_goals_use_case_interface import IGetGoalsUseCase

class GetGoalsUseCase(IGetGoalsUseCase):
    def __init__(self, goals_repository: IGoalRepository):
        self.goals_repository = goals_repository

    def execute(self, user_id: str) -> list:
        result = self.goals_repository.get(user_id)
        
        return GetGoalsOutput([GetGoalsOutputItem(goal.id, goal.name, goal.user, goal.get_current_amount(), goal.target_amount, goal.deadline) for goal in result])