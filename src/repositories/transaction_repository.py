from domain.repositories.transaction_repository_interface import ITransactionRepository
from repositories.sqlalchemy.mappers.transaction_mapper import TransactionMapper
from repositories.sqlalchemy.models.transaction_model import TransactionModel

class TransactionRepository(ITransactionRepository):
    def __init__(self, session_factory):
        self.session_factory = session_factory

    def add(self, transaction):
        with self.session_factory() as session:
            model = TransactionMapper.to_model(transaction)
            session.add(model)
            session.commit()
            session.refresh(model)
            
            return TransactionMapper.to_domain(model)
        
    def update(self, transaction):
        with self.session_factory() as session:
            model = session.query(TransactionModel).filter(TransactionModel.id == transaction.id).first()
            if not model:
                return None
            
            model.amount = transaction.amount
            model.date = transaction.date
            model.category = transaction.category
            model.payment_method = transaction.payment_method
            model.user_id = transaction.user_id
            
            session.commit()
            session.refresh(model)
            return TransactionMapper.to_domain(model)
    
    def delete(self, transaction_id):
        with self.session_factory() as session:
            transaction = session.query(TransactionModel).filter(TransactionModel.id == transaction_id).first()
            
            if transaction:
                session.delete(transaction)
                session.commit()
                return True
            
            return False
        
    def get(self, user_id):
        with self.session_factory() as session:
            transactions: list[TransactionModel] = session.query(TransactionModel).filter(TransactionModel.user_id == user_id).all()
            
            return [TransactionMapper.to_domain(transaction) for transaction in transactions]
        
    def get_by_id(self, transaction_id):
        with self.session_factory() as session:
            transaction = session.query(TransactionModel).filter(TransactionModel.id == transaction_id).first()
            
            return TransactionMapper.to_domain(transaction) if transaction else None
        
    def get_by_user_id(self, user_id):
        with self.session_factory() as session:
            transactions = session.query(TransactionModel).filter(TransactionModel.user_id == user_id).all()
            
            return [TransactionMapper.to_domain(transaction) for transaction in transactions]
        
    def get_by_category(self, category):
        with self.session_factory() as session:
            transactions = session.query(TransactionModel).filter(TransactionModel.category == category).all()
            
            return [TransactionMapper.to_domain(transaction) for transaction in transactions]
        
    def get_by_payment_method(self, payment_method):
        with self.session_factory() as session:
            transactions = session.query(TransactionModel).filter(TransactionModel.payment_method == payment_method).all()
            
            return [TransactionMapper.to_domain(transaction) for transaction in transactions]