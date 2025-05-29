from domain.repositories.category_repository_interface import ICategoryRepository
from domain.entities.category import Category

from repositories.sqlalchemy.mappers.category_mapper import CategoryMapper
from repositories.sqlalchemy.models.category_model import CategoryModel

class CategoryRepository(ICategoryRepository):
    def __init__(self, session_factory):
        self.session_factory = session_factory

    def add(self, category):
        with self.session_factory() as session:
            model = CategoryMapper.to_model(category)
            session.add(model)
            session.commit()
            session.refresh(model)
        
            return CategoryMapper.to_domain(model)
    
    def update(self, category: Category):
        with self.session_factory() as session:
            model = session.query(CategoryModel).filter(CategoryModel.id == category.id).first()
            if not model:
                return None
            
            model.name = category.name
            model.deadline = category.deadline
            model.target_amount = category.target_amount
            model.current_amount = category.get_current_amount()

            session.commit()
            session.refresh(model)
            return CategoryMapper.to_domain(model)
    
    def delete(self, category_id):
        with self.session_factory() as session:
            category = session.query(CategoryModel).filter(CategoryModel.id == category_id).first()
            
            if category:
                session.delete(category)
                session.commit()
                return True
            
            return False
    
    def get(self):
        with self.session_factory() as session:
            categories = session.query(CategoryModel).all()
            return [CategoryMapper.to_domain(category) for category in categories]
    
    def get_by_id(self, category_id):
        with self.session_factory() as session:
            category = session.query(CategoryModel).filter(CategoryModel.id == category_id).first()
            
            if not category:
                return None
            
            return CategoryMapper.to_domain(category)
        
    def get_by_transaction(self, transaction_id):
        with self.session_factory() as session:
            category = session.query(CategoryModel).filter(CategoryModel.transaction_id == transaction_id).first()
            
            if not category:
                return None
            
            return CategoryMapper.to_domain(category)