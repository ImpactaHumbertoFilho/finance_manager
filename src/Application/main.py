#Isso aqui garante que o src sempre fique disponivel... meio gambiarra mas pelo menos fica mais facil kkkk
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#fazer import depois dessa linha

from domain.usecases.delete_user.delete_user_input import DeleteUserInput
from usecases.user.delete_user_use_case import DeleteUserUseCase
from usecases.user.get_user_use_case import GetUserUseCase
from domain.usecases.update_user.update_user_input import UpdateUserInput
from usecases.user.update_user_use_case import UpdateUserUseCase
from domain.usecases.create_user.create_user_input import CreateUserInput
from usecases.user.create_user_use_case import CreateUserUseCase
from repositories.user.user_repository import UserRepository

# Função para instalar todas as dependências
def install_services():
    #Repository
    user_repository = UserRepository()  # Exemplo de repositório

    #useCases
    create_user_use_case = CreateUserUseCase(user_repository)
    update_user_use_case = UpdateUserUseCase(user_repository)
    delete_user_use_case = DeleteUserUseCase(user_repository)
    get_user_use_case = GetUserUseCase(user_repository)
    
    return {
        'create_user_use_case': create_user_use_case,
        'update_user_use_case': update_user_use_case,
        'delete_user_use_case': delete_user_use_case,
        'get_user_use_case': get_user_use_case
    }

# Função principal que orquestra a execução do programa
def main():
    # Instalando as dependências
    services = install_services()

    # Acessando os casos de uso
    create_user_use_case = services['create_user_use_case']
    update_user_use_case = services['update_user_use_case']
    delete_user_use_case = services['delete_user_use_case']
    get_user_use_case = services['get_user_use_case']

    # Exemplo de como utilizar o caso de uso
    input_data = CreateUserInput(name="John Doe", email="john.doe@example.com")
    result = create_user_use_case.execute(input_data)
    print(result)
    
    update_data = UpdateUserInput(result.id, result.email, result.name)
    update_result = update_user_use_case.execute(update_data)
    print(update_result)
    
    delete_data = DeleteUserInput(2)
    delete_result = delete_user_use_case.execute(delete_data)
    print(delete_result)
    
    get_result = get_user_use_case.execute()
    print(get_result)

# Executando o programa
if __name__ == "__main__":
    main()
