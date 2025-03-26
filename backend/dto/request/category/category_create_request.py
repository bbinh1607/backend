from marshmallow import Schema, fields

class CategoryCreateUpdateRequest(Schema):
    name = fields.Str(required=True)
    description = fields.Str(required=False)
