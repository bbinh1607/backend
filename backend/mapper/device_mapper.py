from backend.entities.device import Device
from backend.dto.response.device.device_response import DeviceResponse
from backend.mapper.component_mapper import ComponentMapper

class DeviceMapper:
    def __init__(self):
        self.device_response_schema = DeviceResponse()
        self.component_mapper = ComponentMapper()
    
    def to_device(self, device_request: dict , list_component: list):
        return Device(
            name=device_request['name'],
            barcode=device_request['barcode'],
            category_id=device_request['category_id'],
            list_component=list_component
        )
        
    def to_device_response(self, device_list):
        if not isinstance(device_list, list):
            device_list = [device_list]

        return self.device_response_schema.dump(device_list, many=True)
    