from domain.entities.financial_goal import FinancialGoal

from domain.usecases.financial_goal.create_financial_goal.create_financial_goal_input import CreateFinancialGoalInput
from domain.usecases.financial_goal.create_financial_goal.create_financial_goal_output import CreateFinancialGoalOutput

class FinancialGoalHelper:
    @classmethod
    def from_input(self, input_data: CreateFinancialGoalInput):
        return FinancialGoal(
            name= input_data.name,
            user_id= input_data.user_id,
            target_amount= input_data.target_amount,
            current_amount= input_data.current_amount,
            deadline= input_data.deadline
        )
    
    @classmethod
    def to_output(self, financial_goal: FinancialGoal):
        return CreateFinancialGoalOutput(
            id= financial_goal.id,
            user_id= financial_goal.user_id,
            name= financial_goal.name,
            target_amount= financial_goal.target_amount,
            current_amount= financial_goal.get_current_amount(),
            deadline= financial_goal.deadline,
        )