from sqlalchemy import Column, String, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from backend import db
from sqlalchemy.orm import relationship

class DeviceDetail(db.Model):
    __tablename__ = 'device_detail'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    image = Column(String, nullable=True)
    device_id = Column(UUID(as_uuid=True), ForeignKey('device.id'), nullable=False)
    description = Column(Text, nullable=True)
    
    # Mối quan hệ với Device
    device = relationship('Device', back_populates='device_details')
    
    def __init__(self, image, device_id, description=None):
        self.image = image
        self.device_id = device_id
        self.description = description