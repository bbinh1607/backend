from backend.dto.response.category.category_response import CategoryResponse
from backend.entities.category import Category

class CategoryMapper:
    def __init__(self):
        self.category_response_schema = CategoryResponse()

    def to_category_response(self, category):
        return self.category_response_schema.dump(category) 
        
    def to_category(self, category_request_data: dict):
        category = Category(**category_request_data)
        return category

    
    def to_category_data(self, category_request: Category):
        category_data = {column.name: getattr(category_request, column.name) for column in Category.__mapper__.columns}
        return category_data