from domain.usecases.user.get_user.get_user_use_case_interface import IGetUserUseCase
from domain.repositories.user_repository_interface import IUserRepository
from domain.usecases.user.get_user.get_user_result import GetUserResult

class GetUserUseCase(IGetUserUseCase):
    def __init__(self, user_repository:IUserRepository):
        self.user_repository = user_repository
    
    def execute(self) -> GetUserResult:
        db_users = self.user_repository.get()

        return GetUserResult(db_users)