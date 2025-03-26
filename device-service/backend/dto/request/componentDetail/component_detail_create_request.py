from marshmallow import Schema, fields

class ComponentDetailCreateRequest(Schema):
    component_id = fields.UUID(required=True)
    image = fields.Str(required=True)
    description = fields.Str(required=True)
    
