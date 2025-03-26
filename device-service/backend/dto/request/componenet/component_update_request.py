from marshmallow import Schema, fields

class ComponentUpdateRequest(Schema):
    name = fields.String(required=False)
    barcode = fields.String(required=False)

