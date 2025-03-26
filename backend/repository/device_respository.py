from backend import db
from backend.entities.device import Device
from uuid import UUID
from backend.entities.component import Component
from sqlalchemy.orm import joinedload


class DeviceRepository:
    def __init__(self):
        self.db = db

    def create_device(self, device_request: Device):
        try: 
            self.db.session.add(device_request)
            self.db.session.commit()
            return device_request
        except Exception as e:
            self.db.session.rollback()
            raise e

    
    def get_device_by_id(self, device_id: str):
        try:
            device_data = self.db.session.query(Device).options(joinedload(Device.list_component)).filter(Device.id == device_id).first()
            return device_data
        except Exception as e:
            self.db.session.rollback()
            raise e
    
    def get_all_devices(self, barcode: str, name: str):
        try:
            filter_conditions = []
            if barcode:
                filter_conditions.append(Device.barcode == barcode)
            if name:
                filter_conditions.append(Device.name.ilike(f"%{name}%"))
            device_data = self.db.session.query(Device).options(joinedload(Device.list_component)).filter(*filter_conditions).all()
            return device_data
        except Exception as e:
            self.db.session.rollback()
            raise e
    
    def update_device(self, device_id: str, device_request: Device):
        try:
            device_data = self.db.session.query(Device).filter(Device.id == device_id).first()
            
            for key, value in device_request.__dict__.items():
                if value is not None and key != 'id': 
                    setattr(device_data, key, value)

            self.db.session.commit()  
            return device_data
        except Exception as e:
            self.db.session.rollback() 
            raise e

    def delete_device(self, device_id: str):
        try:
            device_data = self.db.session.query(Device).options(joinedload(Device.list_component)).filter(Device.id == device_id).first()
            self.db.session.delete(device_data)
            self.db.session.commit()
            return True 
        except Exception as e:
            self.db.session.rollback()
            raise e
    
    def delete_device(self, device_id: str):
        try:
            device_data = self.db.session.query(Device).options(joinedload(Device.list_component)).filter(Device.id == device_id).first()

            for component in device_data.list_component:
                self.db.session.delete(component)
                
            self.db.session.delete(device_data)
                
            self.db.session.commit()
            return True
        except Exception as e:
            self.db.session.rollback()  # Nếu có lỗi, rollback để tránh sai sót
            raise e
    