class User:
    _id_counter = 1  # atributo de classe para simular ID automático

    def __init__(self, name: str, email: str, id: int = None):
        self.id = id
        self.name = name
        self.email = email
        self._transactions = []  # encapsulado
        self._goals = []

    def list_transactions(self):
        return self._transactions

    def list_goals(self):
        return self._goals

    def __str__(self):
        return f"User({self.id}) - {self.name} <{self.email}>"
