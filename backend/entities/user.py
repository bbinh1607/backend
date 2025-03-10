from backend import db
from backend.entities.country import Country
from sqlalchemy.orm import relationship
from marshmallow_sqlalchemy import SQLAlchemySchema, SQLAlchemyAutoSchema, auto_field
from backend.entities.refresh_token import RefreshToken


class Profile(db.Model):
    __tablename__ = 'profile'
    
    id = db.Column(db.Integer, primary_key=True)
    birth_date = db.Column(db.Date, nullable=False)
    job = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    user = db.relationship("User", uselist=False, back_populates="profile")


class User(db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)
    
    country = relationship("Country")  # Sửa từ Country.__name__ thành "Country"
    profile = relationship("Profile", uselist=False, back_populates="user")
    refresh_tokens = db.relationship("RefreshToken", back_populates="user", cascade="all, delete-orphan")


class UserSchema(SQLAlchemySchema):
    class Meta:
        model = User
        include_relationships = True
        load_instance = True
        include_fk = True  # Đảm bảo khóa ngoại được nhận diện

    id = auto_field()
    username = auto_field()
    email = auto_field()
    password = auto_field()
    country_id = auto_field() 


class ProfileSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Profile
        include_relationships = True
        load_instance = True
