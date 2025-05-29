from domain.entities.goal import Goal
from domain.repositories.goal_repository_interface import IGoalRepository
from domain.repositories.user_repository_interface import IUserRepository

from domain.usecases.goal.create_goal.create_goal_input import CreateGoalInput
from domain.usecases.goal.create_goal.create_goal_output import CreateGoalOutput
from domain.usecases.goal.create_goal.create_goal_use_case_interface import ICreateGoalUseCase

class CreateGoalUseCase(ICreateGoalUseCase):
    def __init__(self, goal_repository: IGoalRepository, user_repository: IUserRepository):
        self.goal_repository = goal_repository
        self.user_repository = user_repository

    def execute(self, input_data: CreateGoalInput) -> CreateGoalOutput:
        user = self.user_repository.get_by_id(input_data.user_id)

        if user is None:
            raise ValueError("Usuário não encontrado.")

        if input_data.target_amount is None or not isinstance(input_data.target_amount, (int, float)) or input_data.target_amount <= 0:
            raise ValueError("A meta deve ser um número maior que 0.")

        goal = Goal(
            user=user,
            name=input_data.name,
            target_amount=input_data.target_amount,
            deadline=input_data.deadline
        )

        result = self.goal_repository.add(goal)

        return CreateGoalOutput(
            id=result.id,
            user = result.user,
            name=result.name,
            target_amount=result.target_amount,
            current_amount=result.get_current_amount(),
            deadline=result.deadline
        )

