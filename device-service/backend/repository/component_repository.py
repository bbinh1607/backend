from backend.entities.component import Component
from backend import db
from backend.error.business_errors import ComponentNotFound
from sqlalchemy.exc import SQLAlchemyError

class ComponentRepository:
    def __init__(self):
        self.db = db

    def create_component(self, component: Component):
        try:
            self.db.session.add(component)
            self.db.session.commit()
            return component
        except SQLAlchemyError as e:
            self.db.session.rollback()
            raise e
    
    def get_component_by_id(self, id: str):
        try:
            component = self.db.session.query(Component).filter(Component.id == id).first()
            return component
        except Exception as e:
            self.db.session.rollback()
            raise e
    
    def get_all_components(self):
        try:
            components = self.db.session.query(Component).all()
            return components
        except Exception as e:
            self.db.session.rollback()
            raise e
    
    def update_component(self, id: str, component_request):
        try:
            component = self.get_component_by_id(id)
            if component:
                for key, value in component_request.items():
                    if value:
                        setattr(component, key, value)
                self.db.session.commit()
                return component
            return None
        except Exception as e:
            self.db.session.rollback()
            raise e

    
    def delete_component(self, id: str):
        try:
            component = self.get_component_by_id(id)
            if component:
                self.db.session.delete(component)
                self.db.session.commit()
                return True
            return False
        except Exception as e:
            self.db.session.rollback()
            raise e
    
    def get_component_by_barcode(self, barcode: str):
        try:
            components = self.db.session.query(Component).filter(Component.barcode == barcode).all()
            return components
        except Exception as e:
            self.db.session.rollback()
            raise e
    
    def get_component_by_name(self, name: str):
        try:
            component = self.db.session.query(Component).filter(Component.name == name).first()
            return component
        except Exception as e:
            self.db.session.rollback()
            raise e
    

