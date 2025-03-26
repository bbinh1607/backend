from marshmallow import Schema, fields

class DeviceDetailUpdateRequest(Schema):
    device_id = fields.UUID(required=True)
    image = fields.Str(required=True)
    description = fields.Str(required=True)
