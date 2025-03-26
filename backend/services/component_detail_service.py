from backend.repository.component_detail_repository import ComponentDetailRepository
from backend.repository.component_repository import ComponentRepository
from backend.error.business_errors import ComponentNotFound, ComponentDetailNotFound
from backend.mapper.component_detail_mapper import ComponentDetailMapper
from uuid import UUID


class ComponentDetailService:
    def __init__(self):
        self.component_detail_repository = ComponentDetailRepository()
        self.component_repository = ComponentRepository()
        self.component_detail_mapper = ComponentDetailMapper()

    def create_component_detail(self, component_detail_request: dict):
        component_detail = self.component_detail_mapper.to_component_detail(component_detail_request)
        component = self.component_repository.get_component_by_id(component_detail.component_id)
        if component is None:
            raise ComponentNotFound()
        tam = self.component_detail_repository.create_component_detail(component_detail)
        if tam is None:
            raise ComponentNotFound()
        return self.component_detail_mapper.to_component_detail_response(tam)

    def get_component_detail_by_id(self, id: str):
        id = UUID(id)
        tam = self.component_detail_repository.get_component_detail_by_id(id)
        if tam is None:
            raise ComponentDetailNotFound()
        return self.component_detail_mapper.to_component_detail_response(tam)

    def get_component_detail_by_component_id(self, component_id: str):
        tam = self.component_repository.get_component_by_id(component_id)
        if tam is None:
            raise ComponentDetailNotFound()
        return self.component_detail_repository.get_component_detail_by_component_id(component_id)

    def get_all_component_detail(self):
        tams = self.component_detail_repository.get_all_component_detail()
        if tams is None:
            raise ComponentDetailNotFound()
        list_component_detail = []
        for tam in tams:
            list_component_detail.append(self.component_detail_mapper.to_component_detail_response(tam))
        return list_component_detail

    def update_component_detail(self, id: str, component_detail_request: dict):
        id = UUID(id)
        tam = self.component_detail_repository.get_component_detail_by_id(id)
        if tam is None:
            raise ComponentDetailNotFound()
        component_detail = self.component_detail_repository.update_component_detail(id, component_detail_request)
        if component_detail is None:
            raise ComponentDetailNotFound()
        return self.component_detail_mapper.to_component_detail_response(component_detail)

    def delete_component_detail(self, id: str):
        id = UUID(id)
        tam = self.component_detail_repository.get_component_detail_by_id(id)
        if tam is None:
            raise ComponentDetailNotFound()
        return self.component_detail_repository.delete_component_detail(id)
    
    def get_component_detail_by_component_id_and_image(self, component_id: str, image: str):
        tam = self.component_detail_repository.get_component_detail_by_component_id_and_image(component_id, image)
        if tam is None:
            raise ComponentDetailNotFound()
        return self.component_detail_mapper.to_component_detail_response(tam)


