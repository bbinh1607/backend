from marshmallow import Schema, fields

class UserCreateRequest(Schema) :
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    email = fields.Str(required=True)
    country_id = fields.Int(required=True)


