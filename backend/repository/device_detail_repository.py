from backend.entities.device_detail import DeviceDetail
from backend import db  
from sqlalchemy.orm import joinedload

class DeviceDetailRepository:
    def __init__(self):
        self.db = db

    def create_device_detail(self, device_detail: DeviceDetail):
        try:
            self.db.session.add(device_detail)
            self.db.session.commit()
            return self.db.session.query(DeviceDetail).options(joinedload(DeviceDetail.device)).filter(DeviceDetail.id == device_detail.id).first()
        except Exception as e:
            self.db.session.rollback()
            raise e
    
    def get_device_detail_by_id(self, id: str):
        try:
            return self.db.session.query(DeviceDetail).options(joinedload(DeviceDetail.device)).filter(DeviceDetail.id == id).first()
        except Exception as e:
            self.db.session.rollback()
            raise e
    
    def get_all_device_details(self):
        try:
            return self.db.session.query(DeviceDetail).options(joinedload(DeviceDetail.device)).all()
        except Exception as e:
            self.db.session.rollback()
            raise e
    
    def update_device_detail(self, id: str, device_detail: DeviceDetail):
        try:
            self.db.session.query(DeviceDetail).filter(DeviceDetail.id == id).update(device_detail)
            self.db.session.commit()
            return self.db.session.query(DeviceDetail).options(joinedload(DeviceDetail.device)).filter(DeviceDetail.id == id).first()
        except Exception as e:
            self.db.session.rollback()
            raise e
    
    def delete_device_detail(self, id: str):
        try:
            self.db.session.delete(self.get_device_detail_by_id(id))
            self.db.session.commit()
        except Exception as e:
            self.db.session.rollback()
            raise e


