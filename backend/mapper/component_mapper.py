from backend.entities.component import Component
from backend.dto.response.component.component_response import ComponentResponse
from backend.dto.request.componenet.component_create_request import ComponentCreateRequest
from backend.repository.component_repository import ComponentRepository

class ComponentMapper:
    def __init__(self):
        self.component_response_schema = ComponentResponse()

    def to_component(self, component: dict):
        return Component(
            name=component['name'],
            barcode=component['barcode']
        )

    def to_component_response(self, component):
        return self.component_response_schema.dump(component, many=isinstance(component, list))


