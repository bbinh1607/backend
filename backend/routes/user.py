from flask import Blueprint, jsonify, request, make_response
from backend.entities.user import User
from sqlalchemy import insert, select
from backend import db
from werkzeug.security import generate_password_hash
from backend.dto.user_creation import UserCreationSchema
from backend.middlewares.auth_middleware import Authentication

user_bp = Blueprint("users", __name__)
user_creation_schema = UserCreationSchema() 

@user_bp.route("/list", methods=["GET"])    
@Authentication()  # ✅ Mở lại middleware
def get_all_users():
    users = db.session.scalars(select(User)).all()
    return jsonify([{"id": user.id, "username": user.username, "email": user.email} for user in users])



@user_bp.route("/create", methods=["POST"])
# @Authentication()
def create_new_user():
    data = request.json
    user_creation = user_creation_schema.load(data)
    
    db.session.execute(insert(User).values(
        username=user_creation.username,
        password=generate_password_hash(user_creation.password),
        email=user_creation.email,
        country_id=user_creation.country_id 
    ))
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 200

@user_bp.route("/tam/<user_id>", methods=["GET"])
@Authentication()
def get_user_detail(user_id):
    # 1
    # data = User.query.filter(User.id == user_id).one()
    
    # 2
    data = db.session.scalars(select(User).where(User.id == user_id)).one()
    
    return jsonify({"id": data.id, "username": data.username, "email": data.email})
