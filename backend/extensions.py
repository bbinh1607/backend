from flask_sqlalchemy import SQLAlchemy
import os
from backend.config import DATABASE_PATH
db = SQLAlchemy()

def create_database():
    """Chỉ tạo database trong thư mục backend nếu chưa tồn tại"""
    db_folder = os.path.dirname(DATABASE_PATH)

    # Tạo thư mục backend nếu chưa tồn tại
    if not os.path.exists(db_folder):
        os.makedirs(db_folder)
        print(f"Folder created at: {db_folder}")

    # Tạo file database nếu chưa tồn tại
    if not os.path.exists(DATABASE_PATH):
        open(DATABASE_PATH, 'a').close()
        print(f"Database created at: {DATABASE_PATH}")
    else:
        print(f"Database already exists at: {DATABASE_PATH}")