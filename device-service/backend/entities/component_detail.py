from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
import uuid
from backend import db

class ComponentDetail(db.Model):
    __tablename__ = 'component_detail'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    component_id = Column(UUID(as_uuid=True), ForeignKey('component.id'), nullable=False)
    image = Column(String, nullable=False)
    description = Column(String, nullable=False)
    
    def __init__(self, component_id, image, description):
        self.component_id = component_id
        self.image = image
        self.description = description
    