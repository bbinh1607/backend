from backend.services.device_detail_service import DeviceDetailService
from backend.utils.response.response_helper import api_response
from flask import Blueprint, request
from backend.dto.request.device_detail.device_detail_create_request import DeviceDetailCreateRequest
from backend.dto.request.device_detail.device_detail_update_request import DeviceDetailUpdateRequest

device_detail_bp = Blueprint("device_detail", __name__)
device_detail_service = DeviceDetailService()

@device_detail_bp.route('/create', methods=['POST'])
def create_device_detail():
    data = request.get_json()
    device_detail_request = DeviceDetailCreateRequest().load(data)
    return api_response(data=device_detail_service.create_device_detail(device_detail_request))

@device_detail_bp.route('/<uuid:id>', methods=['GET'])
def get_device_detail_by_id(id: str):
    return api_response(data=device_detail_service.get_device_detail_by_id(id))

@device_detail_bp.route('/get-all', methods=['GET'])
def get_all_device_details():
    return api_response(data=device_detail_service.get_all_device_details())

@device_detail_bp.route('/update/<uuid:id>', methods=['PUT'])
def update_device_detail(id: str):
    data = request.get_json()
    device_detail_request = DeviceDetailUpdateRequest().load(data)
    return api_response(data=device_detail_service.update_device_detail(id, device_detail_request))

@device_detail_bp.route('/delete/<uuid:id>', methods=['DELETE'])
def delete_device_detail(id: str):
    return api_response(data=device_detail_service.delete_device_detail(id))
