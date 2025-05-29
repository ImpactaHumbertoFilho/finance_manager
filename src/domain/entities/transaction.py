from datetime import datetime, timedelta
from domain.entities.Installment import Installment
from domain.entities.category import Category
from domain.entities.payment_method import PaymentMethod

class Transaction:
    def __init__(self, value: float, description: str, date, type, user, category, payment_method, id: int = None):
        self.id = id
        self._user = user
        self._category = category
        self._type = type
        self._payment_method = payment_method
        self.value = value
        self.description = description
        self.date = date
        self.installments: list[Installment] = []
    
    def add_installment(self, number: int, amount: float):
        if amount <= 0:
            raise ValueError("O valor da parcela deve ser positivo.")
        
        if number > 1:
            due_date = (datetime.strptime(self.date, '%Y-%m-%d') + timedelta(days=30 * number))
        else:
            due_date = self.date
        
        self.installments.append(Installment(number, amount, due_date))

    @property
    def user(self):
        return self._user
    
    @property
    def category(self) -> Category:
        return self._category
    
    @property
    def type(self):
        return self._type
    
    @property
    def payment_method(self) -> PaymentMethod:
        return self._payment_method
    
    def change_category(self, category: Category):
        if not isinstance(category, Category):
            raise ValueError("Invalid category type.")
        
        self._category = category
    
    def change_payment_method(self, payment_method: PaymentMethod):
        if not isinstance(payment_method, PaymentMethod):
            raise ValueError("Invalid payment method type.")
        
        self._payment_method = payment_method