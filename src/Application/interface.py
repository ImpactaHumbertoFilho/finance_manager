from domain.usecases.user.create_user.create_user_input import CreateUserInput
from domain.usecases.user.delete_user.delete_user_input import DeleteUserInput
from domain.usecases.user.update_user.update_user_input import UpdateUserInput

# Metodo pega o formato CreateUserInput (do tipo Createuserinput)
# Chama o nosso caso de uso em services
#E executa a seguir com encapsulamento

def login(services, email: str, password: str):
    get_users_use_case = services['get_user_use_case']
    users = get_users_use_case.execute()
    for user in users:
        if user.email == email:
            return user

def create_user_method (CreateUserInput: CreateUserInput, services):
    create_user_use_case = services['create_user_use_case']
    user = create_user_use_case.execute(CreateUserInput)
    print(user)

def update_user_method (UpdateUserInput: UpdateUserInput, services):
    update_user_use_case = services['update_user_use_case']
    user = update_user_use_case.execute(UpdateUserInput)
    print(user)

def delete_user_method (DeleteUserInput: DeleteUserInput, services):
    delete_user_use_case = services['delete_user_use_case']
    user = delete_user_use_case.execute(DeleteUserInput)
    print(user)

def get_user_method (services):
    get_user_use_case = services['get_user_use_case']
    user = get_user_use_case.execute()
    print(user)

def create_goal_method (CreateFinancialGoalInput, services):
    create_goal_use_case = services['create_goal_use_case']
    goal = create_goal_use_case.execute(CreateFinancialGoalInput)
    print(goal)

def get_goal_method (services):
    get_goal_use_case = services['get_goal_use_case']
    goal = get_goal_use_case.execute()
    print(goal)