from backend import db
from backend.entities.component_detail import ComponentDetail

class ComponentDetailRepository:
    def __init__(self):
        self.db = db

    def create_component_detail(self, component_detail_request: ComponentDetail):
        try:
            self.db.session.add(component_detail_request)
            self.db.session.commit()    
            return component_detail_request
        except Exception as e:
            self.db.session.rollback()
            raise e
        
    def get_component_detail_by_id(self, id: str):
        try:
            component_detail_data = self.db.session.query(ComponentDetail).filter(ComponentDetail.id == id).first()
            return component_detail_data
        except Exception as e:
            self.db.session.rollback()
            raise e
        
    def get_component_detail_by_component_id(self, component_id: str):
        try:
            component_detail_data = self.db.session.query(ComponentDetail).filter(ComponentDetail.component_id == component_id).all()
            return component_detail_data
        except Exception as e:
            self.db.session.rollback()
            raise e
        
    def get_all_component_detail(self):
        try:
            component_detail_data = self.db.session.query(ComponentDetail).all()
            return component_detail_data
        except Exception as e:
            self.db.session.rollback()
            raise e
        
    def update_component_detail(self, id: str, component_detail_request: dict):
        try:
           component_detail = self.get_component_detail_by_id(id)
           if component_detail:
               for key, value in component_detail_request.items():
                   setattr(component_detail, key, value)
               self.db.session.commit()
               return component_detail
           return None
        except Exception as e:
            self.db.session.rollback()
            raise e
        
    def delete_component_detail(self, id: str):
        try:
            self.db.session.delete(self.get_component_detail_by_id(id))
            self.db.session.commit()
            return True
        except Exception as e:
            self.db.session.rollback()
            return False

