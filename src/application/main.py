#Isso aqui garante que o src sempre fique disponivel... meio gambiarra mas pelo menos fica mais facil kkkk
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#fazer import depois dessa linha
from application.interface import start_app

from usecases.user.delete_user_use_case import DeleteUserUseCase
from usecases.user.get_user_use_case import GetUserUseCase
from usecases.user.update_user_use_case import UpdateUserUseCase
from usecases.user.create_user_use_case import CreateUserUseCase
from usecases.financial_goal.get_financial_goals_use_case import GetFinancialGoalsUseCase
from usecases.financial_goal.create_financial_goal_use_case import CreateFinancialGoalUseCase

from repositories.user_repository import UserRepository
from repositories.financial_goal_repository import FinancialGoalRepository

# Inicializando as models do banco de dados
# Step precisa ser importado antes de iniciar o banco de dados
from repositories.sqlalchemy.models.category_model import CategoryModel
from repositories.sqlalchemy.models.transaction_model import TransactionModel
from repositories.sqlalchemy.models.financial_goal_model import FinancialGoalModel
from repositories.sqlalchemy.models.user_model import UserModel

#inicializando o banco de dados
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
    get_goals_use_case = GetFinancialGoalsUseCase(goal_repository)
    
    return {
        'create_user_use_case': create_user_use_case,
        'update_user_use_case': update_user_use_case,
        'delete_user_use_case': delete_user_use_case,
        'get_user_use_case': get_user_use_case,

        'create_goal_use_case': create_goal_use_case,
        'get_goals_use_case': get_goals_use_case
    }

def main():
    # Conectando/Iniciando o banco de dados
    create_database()
    
    # Instalando as dependências
    services = install_services()

    # Iniciando a aplicação
    start_app(services)

if __name__ == "__main__":
    main()
