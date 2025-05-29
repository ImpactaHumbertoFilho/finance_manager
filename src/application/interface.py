from domain.usecases.goal.add_goal_amount.add_goal_amount_input import AddGoalAmountInput
from domain.usecases.goal.create_goal.create_goal_input import CreateGoalInput
from domain.usecases.goal.update_goal.update_goal_input import UpdateGoalInput
from domain.usecases.installment.create_installment_input import CreateInstallmentInput
from domain.usecases.transaction.create_transaction.create_transaction_Input import CreateTransactionInput
from domain.usecases.user.create_user.create_user_input import CreateUserInput
from domain.usecases.user.delete_user.delete_user_input import DeleteUserInput
from domain.usecases.user.update_user.update_user_input import UpdateUserInput

box_width = 80

def center_text(text: str, width):
    return text.center(width - 4)

def print_error_menu_box(title, error, isInsideSubMenu=False):
    print()
    if not isInsideSubMenu:
        print("+" + "-" * (box_width - 2) + "+")
    
    print("| " + center_text(title, box_width) + " |")
    print("+" + "-" * (box_width - 2) + "+")
    print("| " + center_text(str(error), box_width) + " |")
    print("+" + "-" * (box_width - 2) + "+")
    print("| " + center_text("Tente novamente", box_width) + " |")
    print("+" + "-" * (box_width - 2) + "+")
    print()

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
        if user.email == email and user.password == password:
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
    result = update_user_use_case.execute(update_user_input)
    
    print(result)

def handle_delete_user(services, user):
    print("Deletando o usuario e seus dados...")

    delete_user_input = DeleteUserInput(user.id)
    delete_user_use_case = services['delete_user_use_case']
    result = delete_user_use_case.execute(delete_user_input)

    print(result)

def handle_create_goal(services, user):
    name = input("Digite o nome da meta: ")
    value = float(input("Digite o valor da meta: "))
    date = input("Digite a data da meta (YYYY-MM-DD): ")

    create_goal_input = CreateGoalInput(name, user.id, value, date)
    
    create_goal_use_case = services['create_goal_use_case']
    create_goal_use_case.execute(create_goal_input)
    print("Meta criada com sucesso!")

def handle_update_goal(services, goal_id):
    name = input("Digite o nome da meta: ")
    value = float(input("Digite o valor da meta: "))
    date = input("Digite a data da meta (YYYY-MM-DD): ")

    create_goal_input = UpdateGoalInput(goal_id, name, date, value)
    
    create_goal_use_case = services['update_goal_use_case']
    result = create_goal_use_case.execute(create_goal_input)

    print(result)

def handle_delete_goal(services, goal_id):
    create_goal_use_case = services['delete_goal_use_case']
    result = create_goal_use_case.execute(goal_id)

    print(result)

def handle_add_goal_amount(services, goal_id):
    value = float(input("Digite o valor a ser adicionado: "))

    create_goal_input = AddGoalAmountInput(goal_id, value)
    
    create_goal_use_case = services['add_goal_amount_use_case']
    result = create_goal_use_case.execute(create_goal_input)

    print(result)

def handle_get_goals(services, user):
    get_goals_use_case = services['get_goals_use_case']
    result = get_goals_use_case.execute(user.id)

    return result.goals

def handle_get_transactions(services, user):
    get_transactions_use_case = services['get_transactions_use_case']
    result = get_transactions_use_case.execute(user.id)

    return result.transactions

def handle_create_transaction(services, user):
    description = input("Digite a descrição da transação: ")
    amount = float(input("Digite o valor da transação: "))
    date = input("Digite a data da transação (YYYY-MM-DD): ")

    print_sub_menu_box("Tipo da transação", ["Entrada", "Saída"], isLastSubMenu=False)
    transaction_type = input("Digite o tipo da transação: ")

    categories_menu(services)
    category = input("Digite a categoria da transação: ")

    #payment_methods_menu(services)
    payment_method = input("Digite o método de pagamento da transação: ")

    print_sub_menu_box("parcelas", ["À vista", "Parcelado"], isLastSubMenu= False)
    installment_option = input("Digite a opção de parcelas: ")
    if installment_option == '1':
        installment = 1
    elif installment_option == '2':
        installment = int(input("Digite o número de parcelas: "))
    else:
        print("Opção inválida. Considerando como à vista.")
        installment = 1

    installments = []
    for i in range(installment):
        installment_amount = input(f"Digite o valor da parcela {i + 1}: ") if installment > 1 else amount
        installment_input = CreateInstallmentInput(number = i+1, amount = installment_amount)
        installments.append(installment_input)
    
    create_transaction_input = CreateTransactionInput(user_id=user.id, description=description, amount=amount, date=date, 
        category_id=category, 
        payment_method_id=payment_method,
        installments=installments,
        type=transaction_type
    )
    
    create_transaction_use_case = services['create_transaction_use_case']
    create_transaction_use_case.execute(create_transaction_input)


def list_transactions(services, user):
    transactions = handle_get_transactions(services, user)

    if not transactions:
        print_sub_menu_box("Suas transações", ["Nenhuma transação cadastrada ainda"], isLastSubMenu=False)
        return

    print_sub_menu_box("Suas transações", transactions, isLastSubMenu=False)

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
    print_sub_menu_box("Aqui estão suas metas", goals if len(goals) > 0 else ["Nenhuma meta cadastrada ainda"], isLastSubMenu=False)
    print_sub_menu_box(f"Selecione o que deseja fazer:", [
        "Adicionar meta",
        "Aletrar meta"
    ], isInsideSubMenu=True)

    return goals

def goal_menu():
    print_sub_menu_box("Selecione o que deseja fazer:", [
        "Adicionar valor",
        "Alterar meta",
        "Deletar meta"
    ])

def transactions_menu():
    print_sub_menu_box("Selecione o que deseja fazer:", [
        "Adicionar transação",
        "Listar transações",
        "Gerar relatório",
    ])

def categories_menu(services):
    get_category_use_case = services['get_category_use_case']
    categories_result = get_category_use_case.execute()

    print_sub_menu_box("Categorias", categories_result.categories, isLastSubMenu=False)

def payment_methods_menu(services):
    get_payment_method_use_case = services['get_payment_method_use_case']
    payment_methods_result = get_payment_method_use_case.execute()

    print_sub_menu_box("Categorias", payment_methods_result.payment_methods, isLastSubMenu=False)

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
            print_error_menu_box("Erro ao realizar login/cadastro", e)

    # Loop para o menu principal
    while user:
        index_menu(user)

        try:
            option = input("Digite a opção desejada: ")
            
            if option == '1':
                handle_update_user(services, user)
            elif option == '2':
                print("Confirme que voce realmente quer deletar o usuario! (s/n)")

                confirm = input("Digite 's' para confirmar ou 'n' para cancelar: ")
                if confirm.lower() == 's':
                    handle_delete_user(services, user)
                    user = None
                    print("Usuário deletado com sucesso.")
                else:
                    print("Operação cancelada.")

            elif option == '3':
                while True:
                    transactions_menu()
                    try:
                        option = input("Digite a opção desejada: ")
                        if option == '1':
                            handle_create_transaction(services, user)
                        elif option == '2':
                            list_transactions(services, user)
                        elif option == '3':
                            print("Gerando relatório... (Funcionalidade não implementada)")
                        elif option == '0':
                            break
                        else:
                            print("Opção inválida. Tente novamente.")

                    except Exception as e:
                        print_error_menu_box("Erro ao realizar operações de transação", e)
            
            elif option == '4':
                while True:
                    goals = goals_menu(services, user)
                    try:
                        option = input("Digite a opção desejada: ")

                        if option == '1':
                            handle_create_goal(services, user)
                        elif option == '2':
                            goal_menu()
                            
                            goal_option = input("Digite a opção desejada: ")
                            goal = int(input("Digite a meta desejada: "))
                            
                            if goal_option == '1':
                                handle_add_goal_amount(services, goals[goal - 1].id)
                            elif goal_option == '2':
                                handle_update_goal(services, goals[goal - 1].id)
                            elif goal_option == '3':
                                handle_delete_goal(services, goals[goal - 1].id)
                            else:
                                print("Opção inválida. Tente novamente.")
                        
                        elif option == '0':
                            break
                        else:
                            print("Opção inválida. Tente novamente.")
                    except Exception as e:
                        print_error_menu_box("Erro ao realizar operação de meta", e)
            elif option == '0':
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except Exception as e:
            print_error_menu_box("Erro ao realizar operação", e)