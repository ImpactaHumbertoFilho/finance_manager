class CreateUserInput:
    def __init__(self, name: str, email: str, password: str, verify_password: str = None):
        self.name = name
        self.email = email
        self.password = password
        self.verify_password = verify_password
