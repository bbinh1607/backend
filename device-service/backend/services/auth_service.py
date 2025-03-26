import secrets
import jwt
from datetime import datetime, timedelta
from werkzeug.security import check_password_hash, generate_password_hash
from backend.repository.user_repository import UserRepository
from backend.repository.refresh_token_repository import RefreshTokenRepository
from backend.error.business_errors import UserAlreadyExists
from backend.config import SECRET_KEY
from backend.dto.response.auth.LoginResponseSchema import LoginResponseSchema


class AuthService:
    def __init__(self):
        self.user_repository = UserRepository()
        self.refresh_token_repository = RefreshTokenRepository()

    def login(self, credentials):
        user = self.user_repository.get_user_by_username(credentials.username)
        if not user or not check_password_hash(user.password, credentials.password):
            return "Invalid credentials"

        access_token = jwt.encode({
            "id": str(user.id),  # Đảm bảo là string
            "user_name": user.username,
            "exp": datetime.utcnow() + timedelta(minutes=30)
        }, SECRET_KEY, algorithm="HS512")

        refresh_token = secrets.token_hex(64)
        expires_at = datetime.utcnow() + timedelta(days=7)

        self.refresh_token_repository.create_refresh_token(user.id, refresh_token, expires_at)

        return LoginResponseSchema().dump({
            "access_token": access_token,
            "refresh_token": refresh_token,
        })
    
    def logout(self, refresh_token):
        self.refresh_token_repository.delete_refresh_token(refresh_token)
        return {"message": "Logged out successfully"}

    def register(self, data):
        if self.user_repository.get_user_by_username(data["username"]):
            raise UserAlreadyExists("Username already exists")
        
        new_user = self.user_repository.create_user(
            username=data["username"],
            password=generate_password_hash(data["password"]),
            email=data["email"],
            country_id=data["country_id"],
            birth_date=data["birth_date"],
            job=data["job"]
        )
        return new_user
    
    def refresh_token(self, refresh_token_str):
        refresh_token = self.refresh_token_repository.get_by_token(refresh_token_str)

        if not refresh_token or refresh_token.is_expired():
            return None, "Invalid or expired refresh token"

        new_access_token = jwt.encode({
            "id": refresh_token.user.id,
            "user_name": refresh_token.user.username,
            "exp": datetime.utcnow() + timedelta(minutes=30)
        }, SECRET_KEY, algorithm="HS512")

        return {"access_token": new_access_token}, None
    
    def verify_token(self, token):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS512"])
            return payload
        except jwt.ExpiredSignatureError:
            return None, "Token has expired"
        except jwt.InvalidTokenError:
            return None, "Invalid token"
