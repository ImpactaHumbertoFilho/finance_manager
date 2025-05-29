from domain.entities.Installment import Installment
from repositories.sqlalchemy.models.installment_model import InstallmentModel

class InstallmentMapper:
    @classmethod
    def to_model(self, installment):
        return InstallmentModel(
            number=installment.number,
            amount=installment.amount,
            due_date=installment.due_date,
            transaction_id=installment.transaction_id
        )
    
    @classmethod
    def to_domain(self, model):
        return Installment(
            number=model.number,
            amount=model.amount,
            due_date=model.due_date,
            transaction_id=model.transaction_id
        )