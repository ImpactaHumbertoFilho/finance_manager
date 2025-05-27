from domain.entities.user import User
from domain.repositories.user_repository_interface import IUserRepository
from domain.usecases.user.update_user.update_user_input import UpdateUserInput
from domain.usecases.user.update_user.update_user_result import UpdateUserResult
from domain.usecases.user.update_user.update_user_use_case_interface import IUpdateUserUseCase


class UpdateUserUseCase(IUpdateUserUseCase):
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository
        
    def execute(self, input: UpdateUserInput):
        user = User(input.name, input.email, input.Id)
        
        user_from_id = self.user_repository.get_by_id(input.Id)
        
        if(not user_from_id):
            return None
        
        updated_user = self.user_repository.update(input.Id, user)
        if not updated_user:
            return UpdateUserResult.failure("Erro ao atualizar o usuário")
        
        return UpdateUserResult.success("Usuario atualizado com sucesso")