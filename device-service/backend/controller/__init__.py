from flask import Blueprint
from .user_controller import user_bp
from backend.error.error_handlers import error_bp
from backend.controller.auth_controller import auth_bp
from backend.controller.device_controller import device_bp
from backend.controller.device_detail_controller import device_detail_bp
from backend.controller.category_controller import category_bp
from backend.controller.component_controller import component_bp
from backend.controller.component_detail_controller import component_detail_bp

# Tạo Blueprint tổng hợp tất cả routes
main_bp = Blueprint("main", __name__)

# Đăng ký các route từ các file controller
main_bp.register_blueprint(user_bp, url_prefix="/users")
main_bp.register_blueprint(auth_bp, url_prefix="/auth")
main_bp.register_blueprint(error_bp, url_prefix="/error")
main_bp.register_blueprint(device_bp, url_prefix="/devices")
main_bp.register_blueprint(device_detail_bp, url_prefix="/device-details")
main_bp.register_blueprint(category_bp, url_prefix="/categories")
main_bp.register_blueprint(component_bp, url_prefix="/components")
main_bp.register_blueprint(component_detail_bp, url_prefix="/component-details")

# Nếu muốn nhóm lại tất cả các route dưới "/details", thì đăng ký blueprint chính
device_service_router = Blueprint("device_service_router", __name__)
device_service_router.register_blueprint(main_bp, url_prefix="/device")

def register_controllers(app):
    # app.register_blueprint(device_service_router)
    app.register_blueprint(main_bp)
