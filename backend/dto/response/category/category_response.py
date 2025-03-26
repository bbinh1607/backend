from marshmallow import Schema, fields

class CategoryResponse(Schema):
    id = fields.UUID(required=True)
    name = fields.String(required=True)
    description = fields.String(required=False, allow_none=True) 