class Goal:
    def __init__(self, name: str, target_amount: float, current_amount: float, deadline: str, user, id: int = None):
        self.id = id
        self.name = name
        self.target_amount = target_amount
        self.current_amount = current_amount
        self.deadline = deadline
        self.user = user
    