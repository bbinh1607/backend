from marshmallow import Schema, fields, post_load

from backend.entities.user import User

class LoginRequest(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)
