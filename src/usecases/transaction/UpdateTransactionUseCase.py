from domain.repositories.transaction_repository_interface import ITransactionRepository

class UpdateTransactionUseCase:
    def __init__(self, transaction_repository: ITransactionRepository, user_repository):
        self.transaction_repository = transaction_repository
        self.user_repository = user_repository

    def execute(self, transaction_data):
        transaction = self.transaction_repository.get_by_id(transaction_data.id)
        if not transaction:
            raise ValueError("transação não encontrada")

        result = self.transaction_repository.update(transaction)
        if not result:
            raise ValueError("Erro ao atualizar a transação")

        return transaction