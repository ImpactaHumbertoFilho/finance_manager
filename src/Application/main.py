#Isso aqui garante que o src sempre fique disponivel... meio gambiarra mas pelo menos fica mais facil kkkk
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from domain.usecases.create_user.create_user_input import CreateUserInput
from usecases.user.create_user_use_case import CreateUserUseCase
from repositories.user.user_repository import UserRepository

def install_services():
    user_repository = UserRepository()

    create_user_use_case = CreateUserUseCase(user_repository)
    
    return {
        'create_user_use_case': create_user_use_case,
    }

def main():
    services = install_services()

    create_user_use_case = services['create_user_use_case']

    input_data = CreateUserInput(name="John Doe", email="john.doe@example.com")
    result = create_user_use_case.execute(input_data)
    print(result)

if __name__ == "__main__":
    main()
