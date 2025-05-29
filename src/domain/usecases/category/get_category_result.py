class GetCategoryResultItem:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name

    def __str__(self):
        return self.name
    
class GetCategoryResult:
    def __init__(self, categories):
        self.categories = [GetCategoryResultItem(category.id, category.name) for category in categories]