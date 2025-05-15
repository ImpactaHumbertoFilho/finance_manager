from domain.usecases.delete_user.delete_user_use_case_interface import IDeleteUserUseCase
from domain.usecases.delete_user.delete_user_result import DeleteUserResult
from domain.usecases.delete_user.delete_user_input import DeleteUserInput
from domain.repositories.user_repository_interface import IUserRepository

class DeleteUserUseCase(IDeleteUserUseCase):
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository
    
    def execute(self, input_data: DeleteUserInput) -> DeleteUserResult:
        get_user_by_id_result = self.user_repository.get_by_id(input_data.id)

        if(not get_user_by_id_result):
            return None
        
        db_user = self.user_repository.delete(input_data.id)

        return DeleteUserResult(
            user_id=db_user.id,
            name=db_user.name,
            email=db_user.email
        )
