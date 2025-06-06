# repositories/sqlalchemy/mappers/transaction_mapper.py

from domain.entities.transaction import Transaction
from repositories.sqlalchemy.models.transaction_model import TransactionModel

class TransactionMapper:
    @staticmethod
    def to_domain(model: TransactionModel) -> Transaction:
        return Transaction(
            id=model.id,
            value=model.value,
            description=model.description,
            date=model.date,
            type=model.type,
            user=model.user,
            category=model.category,
            payment_method=model.payment_method
        )

    @staticmethod
    def to_model(entity: Transaction) -> TransactionModel:
        return TransactionModel(
            id=entity.id,
            value=entity.value,
            description=entity.description,
            date=entity.date,
            type=entity.type,
            user_id=entity.user.id,
            category_id=entity.category.id,
            payment_method_id=entity.payment_method.id
        )
