from flask import Blueprint
from backend.routes.health import health_bp
from backend.routes.user import user_bp
from backend.error.error_handlers import error_bp
from backend.routes.auth import auth_bp
from backend.routes.groups import group_bp


# Tạo Blueprint tổng hợp tất cả routes
main_bp = Blueprint("main", __name__)

# Đăng ký các route từ các file khác
main_bp.register_blueprint(health_bp, url_prefix="/health")
main_bp.register_blueprint(user_bp, url_prefix="/users")
main_bp.register_blueprint(error_bp, url_prefix="/error")
main_bp.register_blueprint(auth_bp, url_prefix="/auth")
main_bp.register_blueprint(group_bp, url_prefix="/groups")
