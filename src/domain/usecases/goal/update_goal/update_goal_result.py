from domain.usecases.base.base_result import BaseResult

class UpdateGoalResult(BaseResult):
    def __init__(self, success: bool, message: str, data=None):
        super().__init__(success, message, data)