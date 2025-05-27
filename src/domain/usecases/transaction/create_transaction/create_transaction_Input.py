class CreateTransactionInput:
    def __init__(self, user_id: int, category_id: int, amount: float, description: str):
        self.user_id = user_id
        self.category_id = category_id
        self.amount = amount
        self.description = description