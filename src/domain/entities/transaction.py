from domain.entities.category import Category
from domain.entities.payment_method import PaymentMethod

class Transaction:
    def __init__(self, value: float, description: str, date: str, type: str, user, category: Category, 
        payment_method: PaymentMethod, id: int = None
    ):
        self.id = id
        self.value = value
        self.description = description
        self.date = date
        self.type = type
        self.user = user
        self.category = category
        self.payment_method = payment_method