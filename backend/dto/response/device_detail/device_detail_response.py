from marshmallow import Schema, fields
from backend.dto.response.device.device_response import DeviceResponse

class DeviceDetailResponse(Schema):
    id = fields.UUID(required=True)
    image = fields.Str(required=True)
    description = fields.Str(required=True)
    device = fields.Nested(DeviceResponse, required=True)


