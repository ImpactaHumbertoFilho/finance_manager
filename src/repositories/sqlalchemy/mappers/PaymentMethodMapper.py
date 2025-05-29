from domain.entities.payment_method import PaymentMethod
from repositories.sqlalchemy.models.payment_method import PaymentMethodModel


class PaymentMethodMapper:
    @staticmethod
    def to_model(payment_method):
        return PaymentMethodModel(
            id=payment_method.id,
            name=payment_method.name
        )

    @staticmethod
    def to_domain(model):
        return PaymentMethod(
            id=model.id,
            name=model.name
        )