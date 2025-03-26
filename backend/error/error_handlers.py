from flask import Blueprint, jsonify
from marshmallow import ValidationError
from werkzeug.exceptions import NotFound, HTTPException
from backend.error.business_errors import BusinessError

error_bp = Blueprint("error_handlers", __name__)

@error_bp.app_errorhandler(ValidationError)
def handle_validation_error(error):
    """Xử lý lỗi Validation (400)"""
    return jsonify({"error": "Validation Error", "message": str(error)}), 400

@error_bp.app_errorhandler(NotFound)
def handle_not_found(error):
    """Xử lý lỗi 404 - Không tìm thấy tài nguyên"""
    return jsonify({
        "error": "Resource Not Found",
        "message": "The requested resource is not available.",
        "details": str(error)
    }), 404


@error_bp.app_errorhandler(BusinessError)
def handle_business_error(error):
    """Xử lý lỗi business logic"""
    return jsonify(error.to_dict()), error.status_code

@error_bp.app_errorhandler(Exception)
def handle_general_exception(error):
    """Xử lý lỗi 500 - Internal Server Error"""
    if isinstance(error, HTTPException):
        return jsonify({
            "error": "HTTP Error",
            "message": error.description
        }), error.code

    return jsonify({
        "error": "Internal Server Error",
        "message": "An unknown error occurred. Please check the logs for more details.",
        "details": str(error)
    }), 500
