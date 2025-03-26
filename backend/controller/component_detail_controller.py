from flask import Blueprint, request, jsonify
from backend.services.component_detail_service import ComponentDetailService
from backend.dto.request.componentDetail.component_detail_create_request import ComponentDetailCreateRequest
from backend.dto.request.componentDetail.component_detail_update_request import ComponentDetailUpdateRequest
from backend.utils.response.response_helper import api_response

component_detail_bp = Blueprint('component_detail', __name__)
component_detail_service = ComponentDetailService()

@component_detail_bp.route('/create', methods=['POST'])
def create_component_detail():
    data = request.json
    component_detail = ComponentDetailCreateRequest().load(data)
    return api_response(data=component_detail_service.create_component_detail(component_detail))

@component_detail_bp.route('/get-all', methods=['GET'])
def get_component_detail():
    return api_response(data=component_detail_service.get_all_component_detail())

@component_detail_bp.route('/update/<id>', methods=['PUT'])
def update_component_detail(id):
    data = request.json
    component_detail = ComponentDetailUpdateRequest().load(data)
    return api_response(data=component_detail_service.update_component_detail(id, component_detail))

@component_detail_bp.route('/delete/<id>', methods=['DELETE'])
def delete_component_detail(id):
    return api_response(data=component_detail_service.delete_component_detail(id))

@component_detail_bp.route('/get-by-component-id/<component_id>', methods=['GET'])
def get_component_detail_by_component_id(component_id):
    return api_response(data=component_detail_service.get_component_detail_by_component_id(component_id))

@component_detail_bp.route('/get-by-id/<id>', methods=['GET'])
def get_component_detail_by_id(id):
    return api_response(data=component_detail_service.get_component_detail_by_id(id))
