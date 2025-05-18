from repositories.sqlalchemy.base import SessionLocal
from sqlalchemy.orm import Session

class FinancialGoalRepository(IFinancialGoalRepository):
    def __init__(self):
        self.session: Session = SessionLocal()

    def add(self, transaction_category):
        self.session.add(transaction_category)
        self.session.commit()
        self.session.refresh(transaction_category)
        return transaction_category