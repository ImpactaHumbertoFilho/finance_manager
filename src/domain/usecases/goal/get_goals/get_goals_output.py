class GetGoalsOutputItem:
    def __init__(self, id: int, name: str, user, current_amount: float, target_amount: float, deadline: str, isCompleted: bool):
        self.id = id
        self.name = name
        self.user = user
        self.current_amount = current_amount
        self.target_amount = target_amount
        self.deadline = deadline
        self.isCompleted = isCompleted

    def __str__(self):
        emoji = '✓' if self.isCompleted else '✗'
        
        return f'{emoji} \'{self.name}\' que tem R$ {self.current_amount:.2f} de R$ {self.target_amount:.2f} até {self.deadline}'

class GetGoalsOutput():
    def __init__(self, goals: list[GetGoalsOutputItem]):
        self.goals = goals
    