from backend.entities.device_detail import DeviceDetail
from backend.dto.request.device_detail.device_detail_create_request import DeviceDetailCreateRequest
from backend.dto.response.device_detail.device_detail_response import DeviceDetailResponse
from backend.mapper.device_mapper import DeviceMapper
class DeviceDetailMapper:
    def __init__(self):
        self.device_detail_response_schema = DeviceDetailResponse()
        self.device_mapper = DeviceMapper()

    def to_device_detail(self, device_detail_request: dict):
        return DeviceDetail(
            device_id=device_detail_request.get('device_id'),
            image=device_detail_request['image'],
            description=device_detail_request['description']
        )
    
    def to_device_detail_response(self, device_detail):
        return self.device_detail_response_schema.dump(device_detail, many=isinstance(device_detail, list))
