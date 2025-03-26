from marshmallow import Schema, fields

class ComponentResponse(Schema):
    id = fields.UUID(required=True)
    name = fields.String(required=True)
    barcode = fields.String(required=True) 