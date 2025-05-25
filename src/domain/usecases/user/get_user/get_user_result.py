class GetUserResult():
    def __init__(self, users = []):
        self.users = users
    
    def __str__(self):
        users = []
        
        for user in self.users:
            users.append(f'{user.id:03d}| {user.name} | {user.email}')

            for transaction in user.list_transactions():
                users.append(f'    Transações:')
                users.append(f'    {transaction.id:03d}| {transaction.description} | {transaction.value} | {transaction.date}')
            for goal in user.list_goals():
                users.append(f'    Metas:')
                users.append(f'    {goal.id:03d}| {goal.name} | {goal.current_amount:.2f} de {goal.target_amount:.2f} | {goal.deadline}')

        return '\n'.join(users)