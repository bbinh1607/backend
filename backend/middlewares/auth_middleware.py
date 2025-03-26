import jwt
import re
from flask import request, jsonify, g
from backend.repository.user_repository import UserRepository
from backend.utils.response.response_helper import api_response
from backend.config import SECRET_KEY

user_repository = UserRepository()

# Các route public tĩnh (cố định)
STATIC_PUBLIC_ROUTES = [
    "/users/create",
    "/auth/login",
    "/auth/register",
    "/auth/refresh",
]

# Các pattern route public động (bắt đầu bằng các prefix này)
DYNAMIC_PUBLIC_PATTERNS = [
    # r"^/user.*",                # Tất cả các route bắt đầu bằng /user
    r"^/ca/\d+$",               # Route dạng /ca/<int:id>
    r"^/ca/.*",                 # Tất cả route bắt đầu bằng /ca/
    r"^/api/public.*"           # Các API public khác
]

def is_public_route():
    """Kiểm tra route hiện tại có nằm trong public route hay không."""

    # 1. Kiểm tra các route tĩnh
    if request.path in STATIC_PUBLIC_ROUTES:
        return True

    # 2. Kiểm tra các route động bằng regex
    for pattern in DYNAMIC_PUBLIC_PATTERNS:
        if re.match(pattern, request.path):
            return True

    return False

def authenticate():
    """Middleware xác thực JWT Token cho mọi request."""
    if is_public_route():
        return  # Bỏ qua xác thực cho route public

    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return api_response(status=False, message="Unauthorized", status_code=401)

    token = auth_header.split(" ")[1]

    try:
        decoded_jwt = jwt.decode(token, SECRET_KEY, algorithms=["HS512"])
        username = decoded_jwt.get("user_name") or decoded_jwt.get("sub")

        if not username:
            return api_response(status=False, message="Invalid token", status_code=401)

        user = user_repository.get_user_by_username(username)
        if not user:
            return api_response(status=False, message="Invalid token", status_code=401)

        g.user = user  # Lưu thông tin user vào Flask's g để sử dụng trong API sau

    except jwt.ExpiredSignatureError:
        return api_response(status=False, message="Token expired", status_code=401)
    except jwt.InvalidTokenError:
        return api_response(status=False, message="Invalid token", status_code=401)
    except Exception:
        return api_response(status=False, message="Authentication failed", status_code=401)

# Middleware toàn cục cho Flask
def register_authentication(app):
    app.before_request(authenticate)
