from domain.repositories.payment_method_repository_interface import IPaymentMethodRepository
from repositories.sqlalchemy.mappers.PaymentMethodMapper import PaymentMethodMapper
from repositories.sqlalchemy.models.payment_method import PaymentMethodModel

class PaymentMethodRepository(IPaymentMethodRepository):
    def __init__(self, session_factory):
        self.session_factory = session_factory

    def add(self, payment_method):
        with self.session_factory() as session:
            model = PaymentMethodMapper.to_model(payment_method)
            session.add(model)
            session.commit()
            session.refresh(model)
            
            return PaymentMethodMapper.to_domain(model)
        
    def update(self, payment_method):
        with self.session_factory() as session:
            model = session.query(PaymentMethodModel).filter(PaymentMethodModel.id == payment_method.id).first()
            if not model:
                return None
            
            model.name = payment_method.name
            model.type = payment_method.type
            
            session.commit()
            session.refresh(model)
            return PaymentMethodMapper.to_domain(model)
        
    def delete(self, payment_method_id):
        with self.session_factory() as session:
            payment_method = session.query(PaymentMethodModel).filter(PaymentMethodModel.id == payment_method_id).first()
            
            if payment_method:
                session.delete(payment_method)
                session.commit()
                return True
            
            return False
    
    def get(self):
        with self.session_factory() as session:
            payment_methods: list[PaymentMethodModel] = session.query(PaymentMethodModel).all()
            
            return [PaymentMethodMapper.to_domain(payment_method) for payment_method in payment_methods]
        
    def get_by_id(self, payment_method_id):
        with self.session_factory() as session:
            payment_method = session.query(PaymentMethodModel).filter(PaymentMethodModel.id == payment_method_id).first()
            
            if not payment_method:
                return None
            
            return PaymentMethodMapper.to_domain(payment_method)
        
    def get_by_transaction_id(self, transaction_id):
        with self.session_factory() as session:
            payment_method = session.query(PaymentMethodModel).filter(PaymentMethodModel.transaction_id == transaction_id).first()
            
            if not payment_method:
                return None
            
            return PaymentMethodMapper.to_domain(payment_method)