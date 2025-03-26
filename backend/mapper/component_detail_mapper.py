from backend.entities.component_detail import ComponentDetail
from backend.entities.component import Component
from backend.dto.response.componentDetail.component_detail_response import ComponentDetailResponse

class ComponentDetailMapper:
    def __init__(self):
        self.component_detail_response_schema = ComponentDetailResponse()

        
    def to_component_detail_response(self, component_detail: ComponentDetail):
        return self.component_detail_response_schema.dump(component_detail)

    def to_component_detail(self, component_detail: dict):
        try:
            component_detail = ComponentDetail(**component_detail)
            return component_detail
        except Exception as e:
            raise e
 
    