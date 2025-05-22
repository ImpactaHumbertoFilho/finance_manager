#Isso aqui garante que o src sempre fique disponivel... meio gambiarra mas pelo menos fica mais facil kkkk
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#fazer import depois dessa linha
from domain.usecases.user.delete_user.delete_user_input import DeleteUserInput
from domain.usecases.user.update_user.update_user_input import UpdateUserInput
from domain.usecases.user.create_user.create_user_input import CreateUserInput
from domain.usecases.financial_goal.create_financial_goal.create_financial_goal_input import CreateFinancialGoalInput

from usecases.user.delete_user_use_case import DeleteUserUseCase
from usecases.user.get_user_use_case import GetUserUseCase
from usecases.user.update_user_use_case import UpdateUserUseCase
from usecases.user.create_user_use_case import CreateUserUseCase
from usecases.financial_goal.create_financial_goal_use_case import CreateFinancialGoalUseCase

from repositories.user_repository import UserRepository
from repositories.financial_goal_repository import FinancialGoalRepository

#inicializando as models do banco de dados
from repositories.sqlalchemy.models.category_model import CategoryModel
from repositories.sqlalchemy.models.transaction_model import TransactionModel
from repositories.sqlalchemy.models.financial_goal_model import FinancialGoalModel
from repositories.sqlalchemy.models.user_model import UserModel

from repositories.sqlalchemy.base import SessionLocal, engine, Base

def restart_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

def create_database():
    Base.metadata.create_all(bind=engine)

def install_services():
    #Repository
    user_repository = UserRepository(SessionLocal)
    goal_repository = FinancialGoalRepository(SessionLocal)

    #useCases
    create_user_use_case = CreateUserUseCase(user_repository)
    update_user_use_case = UpdateUserUseCase(user_repository)
    delete_user_use_case = DeleteUserUseCase(user_repository)
    get_user_use_case = GetUserUseCase(user_repository)
    
    create_goal_use_case = CreateFinancialGoalUseCase(goal_repository, user_repository)
    
    return {
        'create_user_use_case': create_user_use_case,
        'update_user_use_case': update_user_use_case,
        'delete_user_use_case': delete_user_use_case,
        'get_user_use_case': get_user_use_case,

        'create_goal_use_case': create_goal_use_case
    }

def main():
    restart_database()
    
    # Instalando as dependências
    services = install_services()

    # Acessando os casos de uso
    create_user_use_case = services['create_user_use_case']
    update_user_use_case = services['update_user_use_case']
    delete_user_use_case = services['delete_user_use_case']
    get_user_use_case = services['get_user_use_case']
    
    create_goal_use_case = services['create_goal_use_case']

    users = [
        {"name": "Alice Smith", "email": "alice.smith@example.com"},
        {"name": "Bob Johnson", "email": "bob.johnson@example.com"},
        {"name": "Carol Williams", "email": "carol.williams@example.com"},
        {"name": "David Brown", "email": "david.brown@example.com"},
        {"name": "Eve Davis", "email": "eve.davis@example.com"},
    ]

    for user in users:
        input_data = CreateUserInput(name=user["name"], email=user["email"])
        create_user_use_case.execute(input_data)
    
    delete_data = DeleteUserInput(2)
    delete_result = delete_user_use_case.execute(delete_data)
    print(delete_result)
    
    input_data = CreateUserInput(name="John Doe", email="john.doe@example.com")
    result = create_user_use_case.execute(input_data)
    
    update_data = UpdateUserInput(result.id, "alterado@gmail.com", "Alterado Da Silva")
    update_result = update_user_use_case.execute(update_data)
    print(update_result)

    goal_data = CreateFinancialGoalInput('Viagem de natal', result.id, 5000.0, '2025-12-20', 1500.0)
    goalResult = create_goal_use_case.execute(goal_data)
    print(goalResult)
    
    get_result = get_user_use_case.execute()
    print(get_result)
    
    try:
        should_fail = CreateUserInput(name="John Doe", email="john.doe@example.com")
        
        create_user_use_case.execute(should_fail)
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
