from domain.usecases.financial_goal.create_financial_goal.create_financial_goal_input import CreateFinancialGoalInput
from domain.usecases.user.create_user.create_user_input import CreateUserInput
from domain.usecases.user.delete_user.delete_user_input import DeleteUserInput
from domain.usecases.user.update_user.update_user_input import UpdateUserInput

box_width = 80

def center_text(text, width):
    return text.center(width - 4)

def print_sub_menu_box(title, options, isInsideSubMenu=False, isLastSubMenu=True):
    if not isInsideSubMenu:
        print("+" + "-" * (box_width - 2) + "+")
    print("| " + center_text(title, box_width) + " |")
    print("+" + "-" * (box_width - 2) + "+")
    
    for i, option in enumerate(options):
        print("| " + center_text(f"{i+1}. {option}", box_width) + " |")

    if isLastSubMenu:
        print("| " + center_text("0. Sair", box_width) + " |")
    
    print("+" + "-" * (box_width - 2) + "+")

def print_menu_box(title, subtitle, options):
    print("+" + "-" * (box_width - 2) + "+")
    print("| " + center_text(title, box_width) + " |")
    print("+" + "-" * (box_width - 2) + "+")
    print("| " + center_text(subtitle, box_width) + " |")
    print("+" + "-" * (box_width - 2) + "+")
    
    for i, option in enumerate(options):
        print("| " + center_text(f"{i+1}. {option}", box_width) + " |")

    print("| " + center_text("0. Sair", box_width) + " |")
    print("+" + "-" * (box_width - 2) + "+")

def get_users(services):
    get_users_use_case = services['get_user_use_case']

    return get_users_use_case.execute()

def handle_login(services):
    print("Insira os dados:")
    email = input("Digite seu email: ")
    password = input("Digite sua senha: ")

    get_users_use_case = services['get_user_use_case']
    result = get_users_use_case.execute()
    for user in result.users:
        if user.email == email:
            return user

def handle_register(services):
    print("Insira os dados:")
    name = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    password = input("Digite sua senha: ")
    verify_password = input("Confirme sua senha: ")
    
    create_user_input = CreateUserInput(name, email, password, verify_password)
    
    create_user_use_case = services['create_user_use_case']
    user = create_user_use_case.execute(create_user_input)

    return user

def handle_update_user(services, user):
    print("Insira os dados:")
    name = input("Digite o novo nome do usuário: ")
    email = input("Digite o novo email do usuário: ")

    update_user_input = UpdateUserInput(user.id, email, name)
    
    update_user_use_case = services['update_user_use_case']
    update_user_use_case.execute(update_user_input)

def handle_delete_user(services, user):
    print("Deletando o usuario e seus dados...")

    delete_user_input = DeleteUserInput(user.id)
    delete_user_use_case = services['delete_user_use_case']
    delete_user_use_case.execute(delete_user_input)

def handle_create_goal(services, user):
    name = input("Digite o nome da meta: ")
    value = float(input("Digite o valor da meta: "))
    date = input("Digite a data da meta (YYYY-MM-DD): ")

    create_goal_input = CreateFinancialGoalInput(name, user.id, value, date)
    
    create_goal_use_case = services['create_goal_use_case']
    create_goal_use_case.execute(create_goal_input)
    print("Meta criada com sucesso!")

def handle_get_goals(services, user):
    get_goals_use_case = services['get_goals_use_case']
    result = get_goals_use_case.execute(user.id)

    return result.goals

def start_menu():
    print_menu_box("Sistema de Gerenciamento Financeiro", "Escolha uma opção:", [
        "Login",
        "Cadastrar usuário"
    ])

def index_menu(user):
    print_menu_box("Sistema de Gerenciamento Financeiro", f"Bem vindo {user.name}. Escolha uma opção:", [
        "Atualizar usuário",
        "Deletar usuário",
        "Transações",
        "metas",
    ])

def goals_menu(services, user):
    goals = handle_get_goals(services, user)
    print_sub_menu_box("Aqui estão suas metas", goals, isLastSubMenu=False)
    print_sub_menu_box(f"Selecione o que deseja fazer:", [
        "Adicionar meta",
        "Aletrar meta"
    ], True)

def goal_menu():
    print_sub_menu_box("Selecione o que deseja fazer:", [
        "Adicionar valor",
        "Alterar meta",
        "Deletar meta"
    ])

def start_app(services):
    user = None

    # Loop para o menu de login/cadastro
    print(get_users(services))
    while True:
        start_menu()

        try:
            answer = input("Digite a opção desejada: ")
            
            if answer == '1':
                user = handle_login(services)
            elif answer == '2':
                user = handle_register(services)
            elif answer == '0':
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida. Tente novamente.")
            
            if user:
                break
            else:
                print("Usuário não encontrado. Tente novamente.")
        except Exception as e:
            print(f"Erro: {e}")
            print("Tente novamente.")

    # Loop para o menu principal
    while user:
        index_menu(user)

        try:
            opcao = input("Digite a opção desejada: ")
            
            if opcao == '1':
                handle_update_user(services, user)
            elif opcao == '2':
                print("Confirme que voce realmente quer deletar o usuario! (s/n)")

                confirm = input("Digite 's' para confirmar ou 'n' para cancelar: ")
                if confirm.lower() == 's':
                    handle_delete_user(services, user)
                    user = None
                    print("Usuário deletado com sucesso.")
                else:
                    print("Operação cancelada.")

            elif opcao == '3':
                while True:
                    goals_menu(services, user)
                    try:
                        opcao = input("Digite a opção desejada: ")

                        if opcao == '1':
                            handle_create_goal(services, user)
                        elif opcao == '2':
                            opcao = input("Digite a meta que deseja alterar: ")
                            goal_menu()

                    except Exception as e:
                        print(f"Erro: {e}")
                        print("Tente novamente.")
            
            elif opcao == '4':
                while True:
                    goals_menu(services, user)
                    try:
                        opcao = input("Digite a opção desejada: ")

                        if opcao == '1':
                            handle_create_goal(services, user)
                        elif opcao == '2':
                            print("Deletar meta (funcionalidade não implementada)")
                            # Aqui você pode implementar a lógica para deletar uma meta
                        elif opcao == '3':
                            print("Adicionar valor a meta (funcionalidade não implementada)")
                            # Aqui você pode implementar a lógica para adicionar valor a uma meta
                        elif opcao == '4':
                            handle_get_goals(services, user)
                        elif opcao == '0':
                            break
                        else:
                            print("Opção inválida. Tente novamente.")
                    except Exception as e:
                        print(f"Erro: {e}")
                        print("Tente novamente.")
            elif opcao == '0':
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except Exception as e:
            print(f"Erro: {e}")
            print("Tente novamente.")