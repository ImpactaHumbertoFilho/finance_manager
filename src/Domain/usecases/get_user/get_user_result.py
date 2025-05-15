class GetUserResult():
    def __init__(self, users = []):
        self.users = users
    
    def __str__(self):
        users = []
        
        for user in self.users:
            users.append(f'{user.id:03d}| {user.name} | {user.email}')
        
        return '\n'.join(users)