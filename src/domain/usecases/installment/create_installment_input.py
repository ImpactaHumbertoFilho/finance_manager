class CreateInstallmentInput:
    def __init__(self, amount: float, number: int):
        self.number = number
        self.amount = amount