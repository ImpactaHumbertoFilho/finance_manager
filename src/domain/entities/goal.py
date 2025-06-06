class Goal:
    def __init__(self, name: str, user, deadline:str, target_amount: float, current_amount = 0, id = None):
        self.id = id
        self._user = user
        self.name = name
        self.deadline = deadline
        self.current_amount = current_amount
        self.target_amount = target_amount
    
    @property
    def current_amount(self) -> float:
        return self.__current_amount
    
    @current_amount.setter
    def current_amount(self, value: float):
        if value < 0:
            raise ValueError("Valor da meta não pode ser negativo.")
        
        self.__current_amount = value

    @property
    def target_amount(self) -> float:
        return self.__target_amount
    
    @target_amount.setter
    def target_amount(self, value: float):
        if value < 0:
            raise ValueError("Valor da meta não pode ser negativo.")
        
        if value < self.__current_amount:
            raise ValueError("Valor da meta não pode ser menor que o valor atual.")

        self.__target_amount = value

    def add_contribution(self, amount: float):
        if amount < 0:
            raise ValueError("Contribuição não pode ser negativa.")
        
        if self.is_goal_achieved():
            raise ValueError("Meta já foi alcançada.")
        
        if self.__current_amount + amount > self.__target_amount:
            raise ValueError("Contribuição excede o valor da meta.")
        
        self.__current_amount += amount

    def get_current_amount(self) -> float:
        return self.__current_amount

    def is_goal_achieved(self) -> bool:
        return self.__current_amount >= self.target_amount
    
    @property
    def user(self):
        return self._user