class CreateFinancialGoalOutput:
    def __init__(self, id: str, user, name: str, target_amount: float, current_amount: float, deadline: str):
        self.id = id
        self.user = user
        self.name = name
        self.target_amount = target_amount
        self.current_amount = current_amount
        self.deadline = deadline

    def __repr__(self):
        return f"CreateFinancialGoalOutput(id={self.id}, user_id={self.user.id}, name={self.name}, target_amount={self.target_amount}, current_amount={self.current_amount}, deadline={self.deadline})"