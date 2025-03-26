
from flask import Blueprint, request
from backend.dto.request.componenet.component_create_request import ComponentCreateRequest
from backend.dto.request.componenet.component_update_request import ComponentUpdateRequest
from backend.services.component_service import ComponentService
from backend.utils.response.response_helper import api_response

component_bp = Blueprint("component", __name__)
component_service = ComponentService()

@component_bp.route('/create', methods=['POST'])
def create_component():
    data = request.json
    component = ComponentCreateRequest().load(data)
    return api_response(data=component_service.create_component(component))

@component_bp.route('/get-all', methods=['GET'])
def get_all_components():
    return api_response(data=component_service.get_all_components())

@component_bp.route('/<uuid:id>', methods=['GET'])
def get_component_by_id(id):
    return api_response(data=component_service.get_component_by_id(id))

@component_bp.route('/get-by-barcode/<barcode>', methods=['GET'])
def get_component_by_barcode(barcode):
    return api_response(data=component_service.get_component_by_barcode(barcode))

@component_bp.route('/get-by-name/<name>', methods=['GET'])
def get_component_by_name(name):
    return api_response(data=component_service.get_component_by_name(name))

@component_bp.route('/update/<uuid:id>', methods=['PUT'])
def update_component(id):
    data = request.json
    component = ComponentUpdateRequest().load(data)
    return api_response(data=component_service.update_component(id, component))

@component_bp.route('/delete/<uuid:id>', methods=['DELETE'])
def delete_component(id):
    return api_response(data=component_service.delete_component(id))