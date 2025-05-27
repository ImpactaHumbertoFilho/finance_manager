class AddGoalAmountInput:
    def __init__(self, goal_id: str, amount: float):
        self.goal_id = goal_id
        self.amount = amount