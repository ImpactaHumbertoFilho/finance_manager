from domain.usecases.transaction.get_transactions.get_transactions_use_case_interface import IGetTransactionsUseCase
from domain.repositories.transaction_repository_interface import ITransactionRepository
from domain.usecases.transaction.get_transactions.get_transactions_result import GetTransactionItem, GetTransactionsResult

class GetTransactionsUseCase(IGetTransactionsUseCase):
    def __init__(self, transaction_repository:ITransactionRepository):
        self.transaction_repository = transaction_repository
    
    def execute(self, user_id) -> GetTransactionsResult:
        db_transactions = self.transaction_repository.get_by_user_id(user_id)

        return GetTransactionsResult([GetTransactionItem(
            value=transaction.value,
            description=transaction.description,
            type=transaction.type,
            user=transaction.user,
            category=transaction.category,
            payment_method=transaction.payment_method,
            date=transaction.date,
            installment=transaction.installments,
            id=transaction.id
        ) for transaction in db_transactions])