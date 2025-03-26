from marshmallow import Schema, fields
from backend.dto.response.component.component_response import ComponentResponse

class DeviceResponse(Schema):
    id = fields.UUID(required=True)
    name = fields.String(required=True)
    barcode = fields.String(required=True)
    category_id = fields.UUID(required=True)
    list_component = fields.Nested(ComponentResponse, many=True, required=True)

