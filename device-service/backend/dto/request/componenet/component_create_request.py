from marshmallow import Schema, fields

class ComponentCreateRequest(Schema):
    name = fields.Str(required=True)
    barcode = fields.Str(required=True)
    