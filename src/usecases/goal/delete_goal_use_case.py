from domain.repositories.goal_repository_interface import IGoalRepository
from domain.usecases.goal.delete_goal.delete_goal_result import DeleteGoalResult

class DeleteGoalUseCase:
    def __init__(self, goal_repository : IGoalRepository):
        self.goal_repository = goal_repository

    def execute(self, goal_id):

        if not goal_id:
            raise ValueError("O ID da meta não pode ser vazio ou nulo.")

        result = self.goal_repository.delete(goal_id)
        if not result:
            return DeleteGoalResult.failure("Erro ao deletar a meta")

        return DeleteGoalResult.success("Meta deletada com sucesso")