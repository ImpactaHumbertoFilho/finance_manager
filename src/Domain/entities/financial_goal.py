class FinancialGoal:
    def __init__(self, name: str, target_amount: float, current_amount: float = 0.0):
        self.name = name
        self.target_amount = target_amount
        self.current_amount = current_amount
    
    def add_contribution(self, amount: float):
        if amount < 0:
            raise ValueError("Contribution amount cannot be negative.")
        self.current_amount += amount

    def is_goal_achieved(self) -> bool:
        return self.current_amount >= self.target_amount