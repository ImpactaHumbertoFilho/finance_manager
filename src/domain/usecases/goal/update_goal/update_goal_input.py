class UpdateGoalInput:
    def __init__(self, goal_id: str, name: str = None, deadline: str = None, target_amount: float = None):
        self.goal_id = goal_id

        self.name = name
        self.deadline = deadline
        self.target_amount = target_amount