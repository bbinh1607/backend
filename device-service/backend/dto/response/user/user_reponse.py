from marshmallow import Schema, fields

class UserResponseSchema(Schema):
    id = fields.Int(required=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    country_id = fields.Int(required=True)