from domain.usecases.base.base_result import BaseResult

class UpdateTransactionResult(BaseResult):
    def __init__(self, success: bool, message: str = "", goal_id: int = None):
        super().__init__(success, message, goal_id)
    
    @classmethod
    def success(cls, goal_id: int):
        return cls(success=True, message="Transação alterada com sucesso", goal_id=goal_id)

    @classmethod
    def failure(cls, message: str):
        return cls(success=False, message=message)