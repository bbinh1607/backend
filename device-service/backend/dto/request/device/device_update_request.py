from marshmallow import Schema, fields

class DeviceUpdateRequest(Schema):
    name = fields.String(required=False)
    barcode = fields.String(required=False)
    category_id = fields.UUID(required=False)
    list_component = fields.List(fields.UUID(), required=False)