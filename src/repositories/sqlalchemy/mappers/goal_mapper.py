from domain.entities.goal import Goal
from repositories.sqlalchemy.models.goal_model import GoalModel

class GoalMapper:
    @staticmethod
    def to_model(entity: Goal) -> GoalModel:
        return GoalModel(
            id=entity.id,
            name=entity.name,
            target_amount=entity.target_amount,
            current_amount=entity.get_current_amount(),
            deadline=entity.deadline,
            user_id=entity.user.id
        )

    @staticmethod
    def to_domain(model: GoalModel) -> Goal:
        return Goal(
            name=model.name,
            target_amount=model.target_amount,
            current_amount=model.current_amount,
            deadline=model.deadline,
            user=model.user,
            id=model.id
        )