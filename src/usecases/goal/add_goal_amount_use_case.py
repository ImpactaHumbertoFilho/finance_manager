from domain.entities.goal import Goal
from domain.repositories.goal_repository_interface import IGoalRepository
from domain.usecases.goal.add_goal_amount.add_goal_amount_input import AddGoalAmountInput
from domain.usecases.goal.add_goal_amount.add_goal_amount_result import AddGoalAmountResult
from domain.usecases.goal.add_goal_amount.add_goal_amount_use_case_interface import IAddGoalAmountUseCase

class AddGoalAmountUseCase(IAddGoalAmountUseCase):
    def __init__(self, goal_repository: IGoalRepository):
        self.goal_repository = goal_repository

    def execute(self, input_data: AddGoalAmountInput):
        goal_id = input_data.goal_id
        amount = input_data.amount

        if not goal_id or amount is None:
            raise ValueError("Valor é obrigatorio")
        
        goal: Goal = self.goal_repository.get_by_id(goal_id)
        if not goal:
            raise ValueError("Meta não encontrada")
        
        goal.add_contribution(input_data.amount)

        updated_goal = self.goal_repository.update(goal)
        if not updated_goal:
            return AddGoalAmountResult.failure("Erro ao atualizar a meta")
        
        return AddGoalAmountResult.success(goal_id=updated_goal.id)