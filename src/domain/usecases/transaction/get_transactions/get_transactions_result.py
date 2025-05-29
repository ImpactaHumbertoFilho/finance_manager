class GetTransactionItem:
    def __init__(self, value: float, description: str, type, user, category, payment_method, date, installment, id):
        self.id = id
        self._user = user
        self._category = category
        self._type = type
        self._payment_method = payment_method
        self.value = value
        self.description = description
        self.date = date
        self.installments = installment

    def __str__(self):
        return f"\'{self.description}\' dia {self.date} no {self._payment_method}, R$ {self.value:.2f} em {len(self.installments)}x vezes"

class GetTransactionsResult:
    def __init__(self, transactions):
        self.transactions = transactions
