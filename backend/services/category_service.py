from backend.repository.category_repository import CategoryRepository
from backend.mapper.category_mapper import CategoryMapper
from backend.error.business_errors import CategoryNotFound

class CategoryService:
    def __init__(self):
        self.category_repository = CategoryRepository()
        self.category_mapper = CategoryMapper()

    def get_all_categories(self):
        tams = self.category_repository.get_all_categories()
        if tams is None:
            raise CategoryNotFound()
        return [self.category_mapper.to_category_response(tam) for tam in tams]

    def get_category_by_id(self, category_id):
        tam = self.category_repository.get_category_by_id(category_id)
        if tam is None:
            raise CategoryNotFound()
        return self.category_mapper.to_category_response(tam)

    def get_category_by_name(self, name):
        tam = self.category_repository.get_category_by_name(name)
        if tam is None:
            raise CategoryNotFound()
        return tam

    def create_category(self, category_request: dict):
        category = self.category_mapper.to_category(category_request)
        tam = self.category_repository.create_category(category)
        if tam is None:
            raise CategoryNotFound()
        return self.category_mapper.to_category_response(tam)

    def update_category(self, category_id, new_data):
        tam = self.category_repository.update_category(category_id, new_data)
        if tam is None:
            raise CategoryNotFound()
        return self.category_mapper.to_category_response(tam)

    def delete_category(self, category_id):
        tam = self.category_repository.delete_category(category_id)
        if tam is None:
            raise CategoryNotFound()
        return tam
