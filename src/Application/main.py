#Isso aqui garante que o src sempre fique disponivel... meio gambiarra mas pelo menos fica mais facil kkkk
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from domain.usecases.create_user.create_user_input import CreateUserInput
from usecases.user.create_user_use_case import CreateUserUseCase
from repositories.user.user_repository import UserRepository

# Função para instalar todas as dependências
def install_services():
    #Repository
    user_repository = UserRepository()  # Exemplo de repositório

    #useCases
    create_user_use_case = CreateUserUseCase(user_repository)
    
    return {
        'create_user_use_case': create_user_use_case,
    }

# Função principal que orquestra a execução do programa
def main():
    # Instalando as dependências
    services = install_services()

    # Acessando os casos de uso
    create_user_use_case = services['create_user_use_case']

    # Exemplo de como utilizar o caso de uso
    input_data = CreateUserInput(name="John Doe", email="john.doe@example.com")
    result = create_user_use_case.execute(input_data)
    print(result)

# Executando o programa
if __name__ == "__main__":
    main()
