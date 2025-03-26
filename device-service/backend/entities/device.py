from backend.entities.component_device import ComponentDevice
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from backend import db
from sqlalchemy.orm import relationship
from backend.entities.category import device_category

class Device(db.Model):
    __tablename__ = 'device'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    barcode = Column(String, nullable=True)
    category_id = Column(UUID(as_uuid=True), ForeignKey('category.id'), nullable=False)

    # Mối quan hệ với Category
    category = relationship('Category', back_populates='devices')

    # Mối quan hệ với Component thông qua bảng trung gian component_device
    list_component = relationship('Component', secondary='component_device', back_populates='devices')
    
    # Mối quan hệ one-to-many với DeviceDetail
    device_details = relationship('DeviceDetail', back_populates='device')

    def __init__(self, name, barcode, category_id, list_component=[]):
        self.name = name
        self.barcode = barcode
        self.category_id = category_id
        self.list_component = list_component

    def __repr__(self):
        return f"<Device(id={self.id}, name='{self.name}', barcode='{self.barcode}')>"

