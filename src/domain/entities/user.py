from domain.entities.transaction import Transaction
from domain.entities.goal import Goal

class User:
    def __init__(self, name: str, email: str, password: str, transactions: list[Transaction] = [], goals:list[Goal] = [], id: int = None):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self._transactions = transactions
        self._goals = goals

    def list_transactions(self):
        return self._transactions

    def list_goals(self):
        return self._goals

    def __str__(self):
        return f"User({self.id}) - {self.name} <{self.email}>"
