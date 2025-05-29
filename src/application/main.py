from application.interface import start_app

from repositories.transaction_repository import TransactionRepository
from usecases.category.get_category_use_case import GetCategoryUseCase
from usecases.user.create_user_use_case import CreateUserUseCase
from usecases.user.delete_user_use_case import DeleteUserUseCase
from usecases.user.get_user_use_case import GetUserUseCase
from usecases.user.update_user_use_case import UpdateUserUseCase
from usecases.goal.get_goals_use_case import GetGoalsUseCase
from usecases.goal.create_goal_use_case import CreateGoalUseCase
from usecases.goal.add_goal_amount_use_case import AddGoalAmountUseCase
from usecases.goal.delete_goal_use_case import DeleteGoalUseCase
from usecases.goal.update_goal_use_case import UpdateGoalUseCase
from usecases.transaction.UpdateTransactionUseCase import UpdateTransactionUseCase
from usecases.transaction.create_transaction_use_case import CreateTransactionUseCase
from usecases.transaction.get_transactions_use_case import GetTransactionsUseCase
from usecases.category.create_category_use_case import CreateCategoryUseCase
from usecases.payment_method.CreatePaymentMethodUseCase import CreatePaymentMethodUseCase

from repositories.user_repository import UserRepository
from repositories.goal_repository import GoalRepository
from repositories.category_repository import CategoryRepository
from repositories.payment_method_repository import PaymentMethodRepository

# Inicializando as models do banco de dados
# Step precisa ser importado antes de iniciar o banco de dados
from repositories.sqlalchemy.models.payment_method import PaymentMethodModel
from repositories.sqlalchemy.models.category_model import CategoryModel
from repositories.sqlalchemy.models.transaction_model import TransactionModel
from repositories.sqlalchemy.models.goal_model import GoalModel
from repositories.sqlalchemy.models.user_model import UserModel

#inicializando o banco de dados
from repositories.sqlalchemy.base import SessionLocal, engine, Base

def install_services():
    #Repository
    user_repository = UserRepository(SessionLocal)
    goal_repository = GoalRepository(SessionLocal)
    transaction_repository = TransactionRepository(SessionLocal)
    category_repository = CategoryRepository(SessionLocal)
    payment_method_repository = PaymentMethodRepository(SessionLocal)
    
    #useCases
    #User Use Cases
    create_user_use_case = CreateUserUseCase(user_repository)
    update_user_use_case = UpdateUserUseCase(user_repository)
    delete_user_use_case = DeleteUserUseCase(user_repository)
    get_user_use_case = GetUserUseCase(user_repository)
    
    #goal Use Cases
    create_goal_use_case = CreateGoalUseCase(goal_repository, user_repository)
    update_goal_use_case = UpdateGoalUseCase(goal_repository, user_repository)
    add_goal_amount_use_case = AddGoalAmountUseCase(goal_repository)
    delete_goal_use_case = DeleteGoalUseCase(goal_repository)
    get_goals_use_case = GetGoalsUseCase(goal_repository)
    
    #transaction Use Cases
    create_transaction_use_case = CreateTransactionUseCase(transaction_repository, user_repository, category_repository, payment_method_repository)
    update_transaction_use_case = UpdateTransactionUseCase(transaction_repository, user_repository)
    get_transactions_use_case = GetTransactionsUseCase(transaction_repository)
    
    #Category Use Cases
    create_category_use_case = CreateCategoryUseCase(category_repository)
    get_category_use_case = GetCategoryUseCase(category_repository)
    
    #Payment_method Use Cases
    create_payment_method_use_case = CreatePaymentMethodUseCase(payment_method_repository)
    
    return {
        'create_user_use_case': create_user_use_case,
        'update_user_use_case': update_user_use_case,
        'delete_user_use_case': delete_user_use_case,
        'get_user_use_case': get_user_use_case,

        'create_goal_use_case': create_goal_use_case,
        'update_goal_use_case': update_goal_use_case,
        'delete_goal_use_case': delete_goal_use_case,
        'add_goal_amount_use_case': add_goal_amount_use_case,
        'get_goals_use_case': get_goals_use_case,

        'create_transaction_use_case': create_transaction_use_case,
        'update_transaction_use_case': update_transaction_use_case,
        'get_transactions_use_case': get_transactions_use_case,

        'create_category_use_case': create_category_use_case,
        'get_category_use_case': get_category_use_case,

        'create_payment_method_use_case': create_payment_method_use_case,
    }

def restart_database(services):
    Base.metadata.drop_all(bind=engine)
    create_database()
    add_data(services)

def create_database():
    Base.metadata.create_all(bind=engine)

def add_data(services):
    try:
        # Adicionando categorias iniciais
        categories = [
            "Alimentação",
            "Transporte",
            "Saúde",
            "Educação",
            "Lazer",
            "Moradia",
            "Serviços",
            "Outros"
        ]
        
        for category_name in categories:
            services['create_category_use_case'].execute(category_name)

        # Adicionando métodos de pagamento iniciais
        payment_methods = [
            "Cartão de Crédito",
            "Cartão de Débito",
            "Dinheiro",
            "Pix"
        ]
        
        for payment_method_name in payment_methods:
            services['create_payment_method_use_case'].execute(payment_method_name)
        
    except Exception as e:
        print(f"Erro ao adicionar dados iniciais: {e}")

def main():
    # Conectando/Iniciando o banco de dados
    #create_database()
    restart_database(services)
    
    # Instalando as dependências
    services = install_services()

    add_data(services)

    # Iniciando a aplicação
    start_app(services)

if __name__ == "__main__":
    main()
