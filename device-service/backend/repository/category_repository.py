from backend import db
from backend.entities.category import Category
from sqlalchemy.exc import SQLAlchemyError
from backend.mapper.category_mapper import CategoryMapper

class CategoryRepository:
    def __init__(self):
        self.db = db
        self.category_mapper = CategoryMapper()

    def get_all_categories(self):
        """Lấy danh sách tất cả danh mục"""
        categories = self.db.session.query(Category).all()
        return categories
    
    def get_category_by_id(self, category_id):
        """Lấy danh mục theo ID"""
        category = self.db.session.query(Category).filter(Category.id == category_id).first()
        return category
    
    def get_category_by_name(self, name):
        """Lấy danh mục theo tên"""
        category = self.db.session.query(Category).filter(Category.name == name).first()
        return category

    def create_category(self, category_request: Category):
        """Tạo danh mục mới"""
        try:
            self.db.session.add(category_request)
            self.db.session.commit()
            return category_request
        except SQLAlchemyError as e:
            self.db.session.rollback()
            raise e
    
    def update_category(self, category_id, new_data):
        """Cập nhật danh mục"""
        try:
            category = self.get_category_by_id(category_id)
            if category:
                for key, value in new_data.items():
                    setattr(category, key, value)  # Cập nhật dữ liệu
                self.db.session.commit()
                return category
            return None  # Trả về None nếu không tìm thấy category
        except SQLAlchemyError as e:
            self.db.session.rollback() 
            raise e

    def delete_category(self, category_id):
        """Xóa danh mục theo ID"""
        try:
            category = self.get_category_by_id(category_id)
            if category:
                self.db.session.delete(category)
                self.db.session.commit()
                return True
            return False  # Không tìm thấy category
        except SQLAlchemyError as e:
            self.db.session.rollback()
            return False
