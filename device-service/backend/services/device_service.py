from backend.repository.device_respository import DeviceRepository
from backend.dto.request.device.device_create_request import DeviceCreateRequest
from backend.dto.request.device.device_update_request import DeviceUpdateRequest
from backend.mapper.device_mapper import DeviceMapper
from backend.repository.component_repository import ComponentRepository
from uuid import UUID
from backend.error.business_errors import DeviceNotFound, ComponentNotFound
from backend.mapper.component_mapper import ComponentMapper

class DeviceService:
    def __init__(self):
        self.device_repository = DeviceRepository()
        self.device_mapper = DeviceMapper()
        self.component_repository = ComponentRepository()
        self.component_mapper = ComponentMapper()

    def create_device(self, device_request: dict):
        try:
            list_component_ids = device_request['list_component']
            
            component_list = []
            for component_id in list_component_ids:
                component = self.component_repository.get_component_by_id(component_id)
                component_list.append(component)
                
            device_data = self.device_mapper.to_device(device_request, component_list)
            self.device_repository.create_device(device_data)
            return self.device_mapper.to_device_response(device_data)
        except Exception as e:
            raise e


    def get_device_by_id(self, device_id: str):
        try:
            device_data = self.device_repository.get_device_by_id(device_id)
            return self.device_mapper.to_device_response(device_data)
        except Exception as e:
            raise e
    
    def get_all_devices(self, barcode: str, name: str):
        try:
            device_data = self.device_repository.get_all_devices(barcode, name) 
            return self.device_mapper.to_device_response1(device_data)  
        except Exception as e:
            raise e

    def update_device(self, device_id: str, device_request: DeviceUpdateRequest):
        try:
            device_data = self.device_repository.get_device_by_id(device_id)
            
            if device_data is None:
                raise DeviceNotFound()

            if 'list_component' in device_request:
                list_component_ids = device_request['list_component']
                component_list = []
                for component_id in list_component_ids:
                    component = self.component_repository.get_component_by_id(component_id)
                    if component:
                        component_list.append(component)
            
                device_data.list_component = component_list 

            device_update = self.device_repository.update_device(device_id, device_data)  
            return self.device_mapper.to_device_response(device_update)
        except Exception as e:
            raise e


    def delete_device(self, device_id: str):
        try:
            self.device_repository.delete_device(device_id)
            return True
        except Exception as e:
            raise e
        
    def add_component(self, device_id: UUID, component_id: str, data: dict):
        try:
            if component_id is None:
                component_request = self.component_mapper.to_component(data)
                component = self.component_repository.create_component(component_request)
            else:
                try:
                    component = self.component_repository.get_component_by_id(UUID(component_id))
                except Exception as e:
                    raise ComponentNotFound()
                    
            device = self.device_repository.get_device_by_id(device_id)
            device.list_component.append(component)
            self.device_repository.update_device(device_id, device)
            
            return self.device_mapper.to_device_response(device)

        except Exception as e:
            raise e

    def remove_component(self, device_id: UUID, component_id: UUID):
        try:
            device = self.device_repository.get_device_by_id(device_id)
            component = self.component_repository.get_component_by_id(component_id)
            if component:
                device.list_component.remove(component)
                self.device_repository.update_device(device_id, device)
                return True
            else:
                raise ComponentNotFound()
        except Exception as e:
            raise e
