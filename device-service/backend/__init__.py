from flask import Flask
from backend.extensions import db, init_extensions
from backend.config import Config
from backend.controller import register_controllers
from backend.middlewares.auth_middleware import register_authentication
from backend.utils.converters.uuid_converter import UUIDConverter
def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)

    init_extensions(app)
    
    app.url_map.converters['uuid'] = UUIDConverter

    with app.app_context():
        db.create_all()  
    
    register_authentication(app)

    register_controllers(app)

    return app
