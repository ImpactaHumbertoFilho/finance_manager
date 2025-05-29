class CreateTransactionInput:
    def __init__(self, user_id: int, category_id: int, payment_method_id: int, type, amount: float, description: str, date, installments):
        self.user_id = user_id
        self.type = type
        self.category_id = category_id
        self.payment_method_id = payment_method_id
        self.amount = amount
        self.description = description
        self.installments = installments
        self.date = date