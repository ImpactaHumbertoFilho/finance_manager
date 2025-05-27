class CreateGoalInput:
    def __init__(self, name: str, user_id:int, target_amount: float, deadline: str, current_amount: float = 0.0):
        self.name = name
        self.user_id = user_id
        self.target_amount = target_amount
        self.deadline = deadline
        self.current_amount = current_amount