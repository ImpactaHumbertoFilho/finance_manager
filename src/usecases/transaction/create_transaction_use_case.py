from domain.usecases.transaction.create_transaction.create_transaction_Input import CreateTransactionInput
from domain.repositories.payment_method_repository_interface import IPaymentMethodRepository
from domain.repositories.transaction_repository_interface import ITransactionRepository
from domain.repositories.category_repository_interface import ICategoryRepository
from domain.repositories.user_repository_interface import IUserRepository
from domain.entities.transaction import Transaction
from repositories.installment_repository import InstallmentRepository

class CreateTransactionUseCase:
    def __init__(self, installment_repository: InstallmentRepository, transaction_repository: ITransactionRepository, user_repository: IUserRepository, category_repository=ICategoryRepository, payment_method_repository=IPaymentMethodRepository):
        self.transaction_repository = transaction_repository
        self.user_repository = user_repository
        self.category_repository = category_repository
        self.payment_method_repository = payment_method_repository
        self.installment_repository = installment_repository

    def execute(self, transaction_data: CreateTransactionInput):
        user = self.user_repository.get_by_id(transaction_data.user_id)
        if not user:
            raise ValueError("Usuario não encontrado")

        category = self.category_repository.get_by_id(transaction_data.category_id)
        if category is None:
            raise ValueError("Categoria não informada")
        
        payment = self.payment_method_repository.get_by_id(transaction_data.payment_method_id)
        if transaction_data.amount <= 0:
            raise ValueError("Valor da transação deve ser maior que zero")
        
        transaction = Transaction(
            user=user,
            type = transaction_data.type,
            value=transaction_data.amount,
            description=transaction_data.description,
            date=transaction_data.date,
            category=category,
            payment_method=payment,
        )

        result = self.transaction_repository.add(transaction)
        if not result:
            raise Exception("Error ao adicionar transação")

        transaction.id = result.id
        for installment in transaction_data.installments:
            transaction.add_installment(
                number=installment.number,
                amount=installment.amount
            )

        result = self.installment_repository.add_many(transaction.installments)
        if not result:
            raise Exception("Error ao adicionar parcelas da transação")
        
        return transaction