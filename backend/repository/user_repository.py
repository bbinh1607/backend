from sqlalchemy import select
from backend.entities.user import Profile, User
from backend import db
from werkzeug.security import generate_password_hash


class UserRepository:
    def get_user_by_username(self, username: str):
        return db.session.scalars(select(User).where(User.username == username)).one()
    
    def get_user_by_id(self, id: int):
        return db.session.scalars(select(User).where(User.id == id)).one()
    
    def create_user(self, username, password, email, country_id, birth_date, job):
        hashed_password = generate_password_hash(password)
        
        new_user = User(username=username, password=hashed_password, email=email, country_id=country_id)
        db.session.add(new_user)
        db.session.flush()  

        new_profile = Profile(user_id=new_user.id, birth_date=birth_date, job=job)
        db.session.add(new_profile)

        db.session.commit()
        return new_user
    
    def update_user(self, user: User):
        db.session.commit()
        return user
    
    def delete_user(self, user: User):
        db.session.delete(user)
        db.session.commit()
        
    def get_all_users(self):
        return db.session.scalars(select(User).all())
    
    