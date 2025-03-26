from marshmallow import Schema, fields

class DeviceCreateRequest(Schema):
    name = fields.String(required=True)
    barcode = fields.String(required=True)
    category_id = fields.UUID(required=True)
    list_component = fields.List(fields.UUID(), required=True)
    