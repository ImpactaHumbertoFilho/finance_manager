class PaymentMethod:
    total = 0

    def __init__(self, name: str, id: int = None):
        self.id = id
        self.name = name
        PaymentMethod.total += 1

    def __repr__(self):
        return f"PaymentMethod(id={self.id}, name={self.name})"