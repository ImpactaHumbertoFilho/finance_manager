#Isso aqui garante que o src sempre fique disponivel... meio gambiarra mas pelo menos fica mais facil kkkk
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#fazer import depois dessa linha
from application.interface import create_goal_method, create_user_method, delete_user_method, get_goal_method, get_user_method, login, update_user_method
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
    create_database()
    
    # Instalando as dependências
    services = install_services()

    # Criando um usuário
    while True:

        print("Bem vindo ao sistema de gerenciamento financeiro!")
        print("1. Cadastre-se")
        print("2. Já tem conta? Faça login")
        answer = input("Digite a opção desejada: ")

        if answer == '1':
            print("Insira os dados:")
            name = input("Digite seu nome: ")
            email = input("Digite seu email: ")
            password = input("Digite sua senha: ")
            create_user_input = CreateUserInput(name, email, password)
            create_user_method(create_user_input, services)

        elif answer == '2':
            email = input("Digite seu email: ")
            password = input("Digite sua senha: ")
            user = login(services, email, password)

        else:
            print("Opção inválida. Tente novamente.")
       
        if user:
            print(f"Bem-vindo, {user.name}!")
            print("Escolha uma opção:")
            print("1. Criar usuário")
            print("2. Listar usuários")
            print("3. Atualizar usuário")
            print("4. Deletar usuário")
            print("5. Criar meta financeira")
            print("6. Listar metas financeiras")
            print("0. Sair do sistema")
            opcao = input("Digite a opção desejada: ")
            
            if opcao == '1':
                print("Insira os dados:")
                name = input("Digite o nome do usuário: ")
                email = input("Digite o email do usuário: ")
                create_user_input = CreateUserInput(name, email)
                create_user_method(create_user_input, services)

            elif opcao == '2':
                get_user_method(services)

            elif opcao == '3':
                print("Insira os dados:")
                name = input("Digite o novo nome do usuário: ")
                email = input("Digite o novo email do usuário: ")
                update_user_input = UpdateUserInput(id, name, email)
                update_user_method(update_user_input, services)

            elif opcao == '4':
                print("Insira os dados:")
                id = input("Digite o id do usuário: ")
                delete_user_input = DeleteUserInput(id)
                delete_user_method(delete_user_input, services)
                
            elif opcao == '5':
                print("Insira os dados:")
                name = input("Digite o nome da meta: ")
                value = input("Digite o valor da meta: ")
                user_id = input("Digite o id do usuário: ")
                create_goal_input = CreateFinancialGoalInput(name, value, user_id)
                create_goal_method(create_goal_input, services)
                
            elif opcao == '6':
                get_goal_method(services)
            elif opcao == '0':
                print("Saindo do sistema...")
                break

if __name__ == "__main__":
    main()
