from domain.usecases.transaction.create_transaction.create_transaction_Input import CreateTransactionInput

class CreateIncomeInput(CreateTransactionInput):
    def __init__(self, amount: float, description: str, date: str):
        self.amount = amount
        self.description = description
        self.date = date

    def __str__(self):
        return f"CreateIncomeInput(amount={self.amount}, description={self.description}, date={self.date})"