class CreateTransactionInput:
    def __init__(self, amount: float, description: str, category_id: str):
        self.amount = amount
        self.description = description
        self.category_id = category_id