from domain.usecases.payment.GetPaymentMethodResult import GetPaymentMethodResult

class GetPaymentMethodUseCase:
    def __init__(self, payment_method_repository):
        self.payment_method_repository = payment_method_repository

    def execute(self):
        payments = self.payment_method_repository.get()

        return GetPaymentMethodResult(payments)