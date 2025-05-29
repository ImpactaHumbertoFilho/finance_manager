from domain.usecases.category.get_category_result import GetCategoryResult

class GetCategoryUseCase:
    def __init__(self, category_repository):
        self.category_repository = category_repository

    def execute(self):
        categories = self.category_repository.get()

        return GetCategoryResult(categories)