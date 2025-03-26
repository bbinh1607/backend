from sqlite3 import IntegrityError
from sqlalchemy import select, insert
from backend import db
from backend.entities.user import User
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import NoResultFound
from backend.mapper.user_mapper import UserMapper
from backend.repository.user_repository import UserRepository
from backend.error.business_errors import  UserAlreadyExists
class UserService:
    def __init__(self):
        self.user_repository = UserRepository()
        self.user_mapper = UserMapper()
        
    def get_all_users(self):
        users = db.session.scalars(select(User)).all()
        return [{"id": user.id, "username": user.username, "email": user.email} for user in users]

    def create_new_user(self, user_creation):
        # Kiểm tra trùng username
        if self.user_repository.get_user_by_username(user_creation.username):
            raise UserAlreadyExists("Username already exists")

        try:
            # Thực hiện insert user
            result = db.session.execute(insert(User).values(
                username=user_creation.username,
                password=generate_password_hash(user_creation.password),
                email=user_creation.email,
                country_id=user_creation.country_id
            ))
            db.session.commit()

            # Lấy user vừa tạo để trả về
            user_id = result.inserted_primary_key[0]
            user = db.session.scalars(select(User).where(User.id == user_id)).one()

            # Sử dụng mapper để chuyển đổi
            return self.user_mapper.to_user_response(user)

        except IntegrityError:
            db.session.rollback()
            raise UserAlreadyExists("Email already exists")

    def get_user_detail(self, user_id):
        try:
            user = db.session.scalars(select(User).where(User.id == user_id)).one()
            return {"id": user.id, "username": user.username, "email": user.email}
        except NoResultFound:
            return {"message": "User not found"}, 404
