import os
from dotenv import load_dotenv

# Load từ file .env
dotenv_path = os.path.join(os.path.abspath(os.getcwd()), ".env")
load_dotenv(dotenv_path)

# Đảm bảo SECRET_KEY được lấy đúng
SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")

# Xác định đường dẫn chính xác cho database trong thư mục backend
basedir = os.path.abspath(os.getcwd())
DATABASE_PATH = os.path.join(basedir, 'backend', 'database.db')

class Config:
    """Cấu hình chung cho ứng dụng"""
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DATABASE_PATH}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
