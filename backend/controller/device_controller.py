from backend.services.device_service import DeviceService
from backend.utils.response.response_helper import api_response
from flask import Blueprint, request
from backend.dto.request.device.device_create_request import DeviceCreateRequest
from backend.dto.request.device.device_update_request import DeviceUpdateRequest
from marshmallow import ValidationError

device_bp = Blueprint("device", __name__)
device_service = DeviceService()

@device_bp.route('/create', methods=['POST'])
def create_device():
    try:
        data = request.get_json()
        device_request = DeviceCreateRequest().load(data)
        device = device_service.create_device(device_request)
        return api_response(status=True, message="Device created successfully", data=device, status_code=201)
    except ValidationError as e:
        return api_response(status=False, message=str(e), status_code=400)


@device_bp.route('/<uuid:id>', methods=['GET'])
def get_device_by_id(id: str):
    return api_response(data=device_service.get_device_by_id(id))


@device_bp.route('/get-all', methods=['GET'])
def get_all_devices():
    barcode = request.args.get('barcode', None)  # Mặc định là rỗng nếu không có 'barcode'
    name = request.args.get('name', None)
    return api_response(data=device_service.get_all_devices(barcode, name), message="Get all devices successfully")


@device_bp.route('/update/<uuid:id>', methods=['PUT'])
def update_device(id: str):
    data = request.get_json()
    device_request = DeviceUpdateRequest().load(data)
    return api_response(data=device_service.update_device(id, device_request))


@device_bp.route('/delete/<uuid:id>', methods=['DELETE'])
def delete_device(id: str):
    return api_response(data=device_service.delete_device(id))


@device_bp.route('/<uuid:device_id>/add-component', methods=['POST'])
def add_component(device_id: str):
    data = request.get_json()
    component_id = request.args.get('component_id', None) 
    return api_response(data=device_service.add_component(device_id, component_id, data))

@device_bp.route('/<uuid:device_id>/remove-component/<uuid:component_id>', methods=['DELETE'])
def remove_component(device_id: str, component_id: str):
    return api_response(data=device_service.remove_component(device_id, component_id))

