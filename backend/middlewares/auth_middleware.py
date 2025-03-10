import jwt
from functools import wraps
from flask import request, jsonify
from backend.repository.user_repository import UserRepository
from backend.utils.response_helper import api_response
from backend.config import SECRET_KEY

user_repository = UserRepository()

def Authentication(required_role=None):
    """ Middleware xác thực JWT Token và kiểm tra vai trò User. """

    def decorator(f):
        @wraps(f)  # Giữ nguyên metadata của hàm gốc
        def wrapped(*args, **kwargs):
            auth_header = request.headers.get("Authorization")

            if not auth_header or not auth_header.startswith("Bearer "):
                return api_response(status=False, message="Unauthorized", status_code=401)

            token = auth_header.split(" ")[1]
            print(token)

            try:
                print("dsadsads")
                decoded_jwt = jwt.decode(token, SECRET_KEY, algorithms=["HS512"])
                print(decoded_jwt)
                username = decoded_jwt.get("user_name")
                print(username)
                if not username:
                    username = decoded_jwt.get("sub")
                user = user_repository.get_user_by_username(username)
                if not user:
                    return api_response(status=False, message="Invalid token", status_code=401)

                if required_role and user.role != required_role:
                    return api_response(status=False, message="Forbidden", status_code=403)

                request.user = user  # Lưu user vào request để sử dụng trong API

            except jwt.ExpiredSignatureError:
                return api_response(status=False, message="Token expired", status_code=401)
            except jwt.InvalidTokenError:
                return api_response(status=False, message="Invalid token", status_code=401)
            except Exception:
                return api_response(status=False, message="Authentication failed", status_code=401)

            return f(*args, **kwargs)

        return wrapped  # Không cần đổi tên function để tránh lỗi Flask
    return decorator
