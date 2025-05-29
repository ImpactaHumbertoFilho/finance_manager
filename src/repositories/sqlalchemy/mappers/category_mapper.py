from repositories.sqlalchemy.models.category_model import CategoryModel


class CategoryMapper:
    @classmethod
    def to_model(cls, category):
        return CategoryModel(
            id=category.id,
            name=category.name,
        )
    
    @classmethod
    def to_domain(cls, model: CategoryModel):
        if not model:
            return None
        
        return CategoryModel(
            id=model.id,
            name=model.name,
        )