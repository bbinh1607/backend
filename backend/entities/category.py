from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from backend import db
from sqlalchemy.orm import relationship

# Định nghĩa bảng trung gian device_category
device_category = Table('device_category', db.Model.metadata,
    Column('device_id', UUID(as_uuid=True), ForeignKey('device.id'), primary_key=True),
    Column('category_id', UUID(as_uuid=True), ForeignKey('category.id'), primary_key=True)
)

class Category(db.Model):
    __tablename__ = 'category'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)

    # Quan hệ one-to-many với Device
    devices = relationship('Device', back_populates='category')

    def __init__(self, name, description=None):
        self.name = name
        self.description = description
