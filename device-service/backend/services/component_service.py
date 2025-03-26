from backend.repository.component_repository import ComponentRepository
from backend.mapper.component_mapper import ComponentMapper
from backend.error.business_errors import ComponentNotFound

class ComponentService:
    def __init__(self):
        self.component_repository = ComponentRepository()
        self.component_mapper = ComponentMapper()

    def create_component(self, component: dict):
        component = self.component_mapper.to_component(component)
        print(component)
        tam = self.component_repository.create_component(component)
        if tam is None:
            raise ComponentNotFound()
        return self.component_mapper.to_component_response(tam)
 
    def get_component_by_id(self, id):
        tam = self.component_repository.get_component_by_id(id)
        if tam is None:
            raise ComponentNotFound()
        return self.component_mapper.to_component_response(tam)

    def get_all_components(self):
        tams = self.component_repository.get_all_components()
        if tams is None:
            raise ComponentNotFound()
        return [self.component_mapper.to_component_response(tam) for tam in tams]

    def update_component(self, id: str, component: dict):
        tam = self.component_repository.update_component(id, component)
        if tam is None:
            raise ComponentNotFound()
        return self.component_mapper.to_component_response(tam)

    def delete_component(self, id: str):
        tam = self.component_repository.delete_component(id)
        if tam is None:
            raise ComponentNotFound()
        return tam

    def get_component_by_barcode(self, barcode: str):
        tams = self.component_repository.get_component_by_barcode(barcode)
        if tams is None:
            raise ComponentNotFound()
        return [self.component_mapper.to_component_response(tam) for tam in tams] 

    def get_component_by_name(self, name: str):
        tam = self.component_repository.get_component_by_name(name)
        if tam is None:
            raise ComponentNotFound()
        return self.component_mapper.to_component_response(tam) 


