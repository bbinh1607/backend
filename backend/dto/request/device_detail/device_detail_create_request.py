from marshmallow import Schema, fields, EXCLUDE, validates, ValidationError

class DeviceDetailCreateRequest(Schema):
    device_id = fields.UUID(required=True)
    image = fields.Str(required=True)
    description = fields.Str(required=True)
    
    class Meta:
        unknown = EXCLUDE  # Bỏ qua bất kỳ trường không được khai báo trong schema

    @validates('device_id')
    def validate_device_id(self, value):
        if not value:
            raise ValidationError('Device ID is required')
        return value

    @validates('image')
    def validate_image(self, value):
        if not value:
            raise ValidationError('Image is required')
        if len(value) <= 1:
            raise ValidationError('Image must be longer than 1 character')
        return value

    @validates('description')
    def validate_description(self, value):
        if not value:
            raise ValidationError('Description is required')
        if len(value) < 1:
            raise ValidationError('Description must be at least 1 character')
        if len(value) > 1000:
            raise ValidationError('Description must be less than 1000 characters')
        return value
