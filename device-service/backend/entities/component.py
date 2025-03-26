from backend.entities.component_device import ComponentDevice
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from backend import db
from sqlalchemy.orm import relationship

class Component(db.Model):
    __tablename__ = 'component'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    barcode = Column(String, nullable=True)

    # Mối quan hệ với Device thông qua bảng trung gian component_device
    devices = relationship('Device', secondary='component_device', back_populates='list_component')

    def __init__(self, name, barcode):
        self.name = name
        self.barcode = barcode

    def __repr__(self):
        return f"<Component(id={self.id}, name='{self.name}', barcode='{self.barcode}')>"