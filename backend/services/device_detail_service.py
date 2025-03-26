from backend.repository.device_detail_repository import DeviceDetailRepository
from backend.entities.device_detail import DeviceDetail
from backend.dto.request.device_detail.device_detail_create_request import DeviceDetailCreateRequest
from backend.repository.device_respository import DeviceRepository
from backend.mapper.device_detail_mapper import DeviceDetailMapper
from backend.error.business_errors import DeviceNotFound
from backend.dto.request.device_detail.device_detail_update_request import DeviceDetailUpdateRequest

class DeviceDetailService:
    def __init__(self):
        self.device_detail_repository = DeviceDetailRepository()
        self.device_repository = DeviceRepository()
        self.device_detail_mapper = DeviceDetailMapper()

    def create_device_detail(self, device_detail: dict):
        try:
            device_detail_data = self.device_detail_mapper.to_device_detail(device_detail)
            device = self.device_repository.get_device_by_id(device_detail_data.device_id)
            if not device:
                raise DeviceNotFound()
            device_detail_data = self.device_detail_repository.create_device_detail(device_detail_data)
            print(self.device_detail_mapper.to_device_detail_response(device_detail_data) , "đây là kết quả")
            return self.device_detail_mapper.to_device_detail_response(device_detail_data)
        except Exception as e:
            raise e
    
    def get_device_detail_by_id(self, id: str):
        try:
            device_detail_data = self.device_detail_repository.get_device_detail_by_id(id)
            return self.device_detail_mapper.to_device_detail_response(device_detail_data)
        except Exception as e:
            raise e
    
    def get_all_device_details(self):
        try:
            device_detail_data = self.device_detail_repository.get_all_device_details()
            return self.device_detail_mapper.to_device_detail_response(device_detail_data)
        except Exception as e:
            raise e
    
    def update_device_detail(self, id: str, device_detail: DeviceDetailUpdateRequest):
        try:
            device_detail_data = self.device_detail_repository.get_device_detail_by_id(id)
            if not device_detail_data:
                raise DeviceNotFound()
            device_detail_data = self.device_detail_repository.update_device_detail(id, device_detail)
            return self.device_detail_mapper.to_device_detail_response(device_detail_data)
        except Exception as e:
            raise e
    
    def delete_device_detail(self, id: str):
        try:
            self.device_detail_repository.delete_device_detail(id)
            return True
        except Exception as e:
            raise e
