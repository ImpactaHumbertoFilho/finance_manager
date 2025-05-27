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
from usecases.goal.get_goals_use_case import GetGoalsUseCase
from usecases.goal.create_goal_use_case import CreateGoalUseCase
from usecases.goal.add_goal_amount_use_case import AddGoalAmountUseCase
from usecases.goal.delete_goal_use_case import DeleteGoalUseCase
from usecases.goal.update_goal_use_case import UpdateGoalUseCase

from repositories.user_repository import UserRepository
from repositories.goal_repository import GoalRepository

# Inicializando as models do banco de dados
# Step precisa ser importado antes de iniciar o banco de dados
from repositories.sqlalchemy.models.category_model import CategoryModel
from repositories.sqlalchemy.models.transaction_model import TransactionModel
from repositories.sqlalchemy.models.goal_model import GoalModel
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
    goal_repository = GoalRepository(SessionLocal)

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
    
    return {
        'create_user_use_case': create_user_use_case,
        'update_user_use_case': update_user_use_case,
        'delete_user_use_case': delete_user_use_case,
        'get_user_use_case': get_user_use_case,

        'create_goal_use_case': create_goal_use_case,
        'update_goal_use_case': update_goal_use_case,
        'delete_goal_use_case': delete_goal_use_case,
        'add_goal_amount_use_case': add_goal_amount_use_case,
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
