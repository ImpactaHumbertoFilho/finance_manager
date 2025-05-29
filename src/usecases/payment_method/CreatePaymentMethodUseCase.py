from domain.repositories.payment_method_repository_interface import IPaymentMethodRepository
from domain.entities.payment_method import PaymentMethod

class CreatePaymentMethodUseCase:
    def __init__(self, payment_method_repository: IPaymentMethodRepository):
        self.payment_method_repository = payment_method_repository

    def execute(self, payment_method_name):
        payment_method = PaymentMethod(name=payment_method_name)

        result = self.payment_method_repository.add(payment_method)
        if not result:
            raise Exception("Falha ao criar metodo de pagamento")
        
        return result