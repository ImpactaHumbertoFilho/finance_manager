class DeleteUserResult():
    def __init__(self, user_id: int, name: str, email: str):
        self.id = user_id
        self.name = name
        self.email = email

    def __str__(self):
        return (
            f"Id: {self.id}\n"
            f"Name: {self.name}\n"
            f"Email: {self.email}"
        )