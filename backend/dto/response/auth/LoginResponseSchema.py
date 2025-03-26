from marshmallow import Schema, fields

class LoginResponseSchema(Schema):
    access_token = fields.Str(required=True)
    refresh_token = fields.Str(required=True)
