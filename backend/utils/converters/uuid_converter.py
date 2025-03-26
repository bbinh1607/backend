from werkzeug.routing import BaseConverter
import uuid

class UUIDConverter(BaseConverter):
    def to_python(self, value):
        return uuid.UUID(value)

    def to_url(self, value):
        return str(value)
