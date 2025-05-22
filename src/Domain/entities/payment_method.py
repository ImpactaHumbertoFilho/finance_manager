class PaymentMethod:
    def __init__(self, name: str, id: int = None):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"PaymentMethod(id={self.id}, name={self.name})"