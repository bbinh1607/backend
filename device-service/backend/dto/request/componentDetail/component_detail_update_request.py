from marshmallow import Schema, fields

class ComponentDetailUpdateRequest(Schema):
    component_id = fields.UUID(required=True)
    image = fields.Str(required=True)
    description = fields.Str(required=True)
    
