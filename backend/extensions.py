from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
from backend.config import DATABASE_PATH

# Khởi tạo các extension
db = SQLAlchemy()
cors = CORS()

# Danh sách các domain được phép truy cập
ALLOWED_ORIGINS = [
    "http://localhost:1.1.1.3000",
    "http://localhost:4000",
    "http://localhost:3000",
    "http://mywebsite.com",
    "https://anotherwebsite.com"
]

def create_database():
    """Chỉ tạo database trong thư mục backend nếu chưa tồn tại"""
    db_folder = os.path.dirname(DATABASE_PATH)

    if not os.path.exists(db_folder):
        os.makedirs(db_folder)

    if not os.path.exists(DATABASE_PATH):
        open(DATABASE_PATH, 'a').close()

def init_extensions(app):
    """Khởi tạo tất cả các extensions với Flask app"""
    create_database()
    
    db.init_app(app)
    
    cors.init_app(app, resources={r"/*": {"origins": ALLOWED_ORIGINS}})
