from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from backend import db

class ComponentDevice(db.Model):
    __tablename__ = 'component_device'

    component_id = Column(UUID(as_uuid=True), ForeignKey('component.id'), primary_key=True)
    device_id = Column(UUID(as_uuid=True), ForeignKey('device.id'), primary_key=True)

    def __init__(self, component_id, device_id):
        self.component_id = component_id
        self.device_id = device_id
