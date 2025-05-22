from domain.entities.financial_goal import FinancialGoal
from repositories.sqlalchemy.models.financial_goal_model import FinancialGoalModel

class FinancialGoalMapper:
    @staticmethod
    def to_model(entity: FinancialGoal) -> FinancialGoalModel:
        return FinancialGoalModel(
            id=entity.id,
            name=entity.name,
            target_amount=entity.target_amount,
            current_amount=entity.get_current_amount(),
            deadline=entity.deadline,
            user_id=entity.user.id
        )

    @staticmethod
    def to_domain(model: FinancialGoalModel) -> FinancialGoal:
        return FinancialGoal(
            name=model.name,
            target_amount=model.target_amount,
            current_amount=model.current_amount,
            deadline=model.deadline,
            user=model.user,
            id=model.id
        )