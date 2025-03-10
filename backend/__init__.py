from flask import Flask
from backend.extensions import db, create_database
from backend.routes import main_bp
from backend.config import Config

def create_app():
    app = Flask(__name__)
    create_database()
    app.config.from_object(Config)
    
    db.init_app(app)  # Chỉ bind db với app tại đây

    with app.app_context():
        db.create_all()  # Tạo bảng (nếu chưa có)  
    
    if "main" not in app.blueprints:
        app.register_blueprint(main_bp)
    
    return app
