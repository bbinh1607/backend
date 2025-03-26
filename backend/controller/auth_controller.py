from flask import Blueprint, request, jsonify
from backend.services.auth_service import AuthService
from backend.dto.request.auth.login_request import LoginRequest
from backend.entities.user import UserSchema
from backend.utils.response.response_helper import api_response

auth_bp = Blueprint("auth", __name__)
auth_service = AuthService()    
login_request = LoginRequest()
user_schema = UserSchema()


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    credentials = login_request.load(data)
    response = auth_service.login(credentials)

    return api_response(data=response, message="Login successful", status_code=200)


@auth_bp.route("/logout", methods=["POST"])
def logout():
    data = request.json
    refresh_token = data.get("refresh_token")

    if not refresh_token:
        return api_response(status=False, message="Refresh token is required", status_code=400)

    response = auth_service.logout(refresh_token)
    return api_response(data=response, message="Logout successful", status_code=200)


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    required_fields = ["username", "password", "email", "country_id", "birth_date", "job"]

    if not all(field in data for field in required_fields):
        return api_response(status=False, message="Missing required fields", status_code=400)

    try:
        new_user = auth_service.register(data)
        return api_response(data=user_schema.dump(new_user), message="User registered successfully", status_code=201)
    except Exception as e:
        return api_response(status=False, message=str(e), status_code=500)

@auth_bp.route("/refresh", methods=["POST"])
def refresh():
    data = request.json
    refresh_token_str = data.get("refresh_token")

    if not refresh_token_str:
        return api_response(status=False, message="Refresh token is required", status_code=400)

    response, error = auth_service.refresh_token(refresh_token_str)
    if error:
        return api_response(status=False, message=error, status_code=401)

    return api_response(data=response, message="Token refreshed successfully", status_code=200)

@auth_bp.route("/verify-token", methods=["POST"])
def verify_token():
    data = request.json
    token = data.get("token")
    return api_response(data=auth_service.verify_token(token))
