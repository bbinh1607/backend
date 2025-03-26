from marshmallow import Schema, fields, post_load, validates, ValidationError
from backend.entities.user import User
import re

class UserCreateRequest(Schema) :
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    email = fields.Str(required=True)
    country_id = fields.Int(required=True)

    @validates("password")
    def validate_password(self, value):
        if len(value) < 8:
            raise ValidationError("Password must be at least 8 characters long")
        if not any(char.isdigit() for char in value):
            raise ValidationError("Password must contain at least one digit")
        if not any(char.isupper() for char in value):
            raise ValidationError("Password must contain at least one uppercase letter")
        if not any(char.islower() for char in value):
            raise ValidationError("Password must contain at least one lowercase letter")

    @validates("email")
    def validate_email(self, value):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValidationError("Invalid email address")
    
    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)