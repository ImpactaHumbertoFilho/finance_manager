from datetime import datetime, timedelta

class Installment:
    def __init__(self, number: int, amount: float, due_date: str):
        self.number = number
        self.amount = amount
        self.due_date = due_date
        
    def __repr__(self):
        return f"Installment(number={self.number}, amount={self.amount}, due_date={self.due_date})"