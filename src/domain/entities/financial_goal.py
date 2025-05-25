class FinancialGoal:
    def __init__(self, name: str, user, deadline:str, target_amount: float, current_amount: float = 0.0, id = None):
        self.id = id
        self._user = user
        self.name = name
        self.deadline = deadline
        self.__target_amount = target_amount
        self.__current_amount = current_amount
    
    @property
    def target_amount(self) -> float:
        return self.__target_amount
    
    @target_amount.setter
    def target_amount(self, value: float):
        if value < 0:
            raise ValueError("Target amount cannot be negative.")
        self.__target_amount = value

    def add_contribution(self, amount: float):
        if amount < 0:
            raise ValueError("Contribution amount cannot be negative.")
        self.__current_amount += amount

    def get_current_amount(self) -> float:
        return self.__current_amount

    def is_goal_achieved(self) -> bool:
        return self.__current_amount >= self.target_amount
    
    @property
    def user(self):
        return self._user