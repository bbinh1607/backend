from backend.services.category_service import CategoryService
from flask import Blueprint, request
from backend.dto.request.category.category_create_request import CategoryCreateUpdateRequest
from backend.utils.response.response_helper import api_response

category_bp = Blueprint("category", __name__)
category_service = CategoryService()

@category_bp.route("/list", methods=["GET"])
def get_all_categories():
    return api_response(data=category_service.get_all_categories())

@category_bp.route("/<uuid:id>", methods=["GET"])
def get_category_by_id(id):
    return api_response(data=category_service.get_category_by_id(id))

@category_bp.route("/create", methods=["POST"])
def create_category():
    try:
        data = request.get_json()
        result = category_service.create_category(data)
        return api_response(data=result)
    except Exception as e:
        return api_response(message=str(e))

@category_bp.route("/update/<uuid:id>", methods=["PUT"])
def update_category(id):
    data = request.get_json()
    category = CategoryCreateUpdateRequest().load(data)
    return api_response(data=category_service.update_category(id, category))

@category_bp.route("/delete/<uuid:id>", methods=["DELETE"])
def delete_category(id):
    return api_response(data=category_service.delete_category(id))

