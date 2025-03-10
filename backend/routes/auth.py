import secrets
from flask import Blueprint, request, jsonify
import jwt
import datetime
from werkzeug.security import check_password_hash
from backend.dto.credentials import CredentialsSchema
from backend.repository.refresh_token_repository import RefreshTokenRepository
from backend.repository.user_repository import UserRepository
from backend.entities.user import UserSchema
from backend.config import SECRET_KEY

auth_bp = Blueprint("auth", __name__)
credentials_schema = CredentialsSchema()
user_repository = UserRepository()
refresh_token_repository = RefreshTokenRepository()
user_schema = UserSchema()

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    credentials = credentials_schema.load(data)
    
    # Kiểm tra user có tồn tại không
    user = user_repository.get_user_by_username(credentials.username)
    if not user or not check_password_hash(user.password, credentials.password):
        return jsonify({"error": "Invalid credentials"}), 401
    
    # Tạo Access Token (30 phút)
    access_token = jwt.encode(
        {"id" : user.id,
         "user_name": user.username, 
         "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
        SECRET_KEY,
        algorithm="HS512"
    )

    # Tạo Refresh Token (dài hạn, random string)
    refresh_token = secrets.token_hex(64)  # Tạo token 64 ký tự hex
    refresh_token_repository.create_refresh_token(user.id, refresh_token)

    return jsonify({"access_token": access_token, "refresh_token": refresh_token})


@auth_bp.route("/logout", methods=["POST"])
def logout():
    data = request.json
    refresh_token = data.get("refresh_token")

    if refresh_token:
        RefreshTokenRepository.delete_refresh_token(refresh_token)

    return jsonify({"message": "Logged out successfully"}),200  



@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    
    # Kiểm tra đầu vào
    required_fields = ["username", "password", "email", "country_id", "birth_date", "job"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    # Tạo tài khoản
    try:
        new_user = UserRepository.create_user(
            username=data["username"],
            password=data["password"],
            email=data["email"],
            country_id=data["country_id"],
            birth_date=data["birth_date"],
            job=data["job"]
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(user_schema.dump(new_user)), 201