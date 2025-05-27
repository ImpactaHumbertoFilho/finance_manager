class BaseResult:
    def __init__(self, success: bool, message: str = "", data = None):
        self.success = success
        self.message = message
        self.data = data if data is not None else {}

    @classmethod
    def success(self, message: str):
        return self(success=True, message=message)

    @classmethod
    def failure(self, message: str):
        return self(success=False, message=message)
    
    def __str__(self):
        if self.success:
            return f"Sucesso: {self.message}"
        else:
            return f"Falha: {self.message}"