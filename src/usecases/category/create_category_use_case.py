from domain.entities.category import Category
from domain.repositories.category_repository_interface import ICategoryRepository

class CreateCategoryUseCase:
    def __init__(self, category_repository: ICategoryRepository):
        self.category_repository = category_repository

    def execute(self, category_name):
        category = Category(name=category_name)

        result = self.category_repository.add(category)
        if not result:
            raise Exception("Falha ao criar a categoria")
        
        return result