from marshmallow import Schema, fields
from backend.dto.response.component.component_response import ComponentResponse

class ComponentDetailResponse(Schema):
    id = fields.UUID(required=True)
    component_id = fields.UUID(required=True)
    image = fields.String(required=True)
    description = fields.String(required=True)
    component = fields.Nested(ComponentResponse, required=True)

