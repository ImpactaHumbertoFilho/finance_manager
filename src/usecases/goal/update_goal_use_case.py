from domain.repositories.goal_repository_interface import IGoalRepository
from domain.repositories.user_repository_interface import IUserRepository
from domain.usecases.goal.update_goal.update_goal_result import UpdateGoalResult
from domain.usecases.goal.update_goal.update_goal_use_case_interface import IUpdateGoalUseCase

class UpdateGoalUseCase(IUpdateGoalUseCase):
    def __init__(self, goal_repository: IGoalRepository, user_repository: IUserRepository):
        self.goal_repository = goal_repository
        self.user_repository = user_repository

    def execute(self, updated_goal_input):
        if not updated_goal_input:
            raise ValueError("Meta precisa ser informada")

        goal = self.goal_repository.get_by_id(updated_goal_input.goal_id)
        if not goal:
            raise ValueError("Meta não encontrada")
        
        goal.name = updated_goal_input.name if updated_goal_input.name is not None else goal.name
        goal.deadline = updated_goal_input.deadline if updated_goal_input.deadline is not None else goal.deadline
        goal.target_amount = updated_goal_input.target_amount if updated_goal_input.target_amount is not None else goal.target_amount
        
        result = self.goal_repository.update(goal)
        if not result:
            raise ValueError("Erro ao atualizar a meta")
        
        return UpdateGoalResult.success("Meta atualizada com sucesso")