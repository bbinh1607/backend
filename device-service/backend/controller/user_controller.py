from flask import Blueprint, request
from backend.services.user_service import UserService
from backend.dto.request.user.user_create_request import UserCreateRequest
from backend.utils.response.response_helper import api_response

class UserController:
    def __init__(self):
        self.user_bp = Blueprint("users", __name__)
        self.user_create_request = UserCreateRequest()
        self.user_service = UserService()
        self.register_routes()

    def register_routes(self):
        self.user_bp.route("/list", methods=["GET"])(
            (self.get_all_users)
        )
        
        self.user_bp.route("/create", methods=["POST"])(
            (self.create_new_user)
        )
        
        self.user_bp.route("/detail/<user_id>", methods=["GET"])(
            (self.get_user_detail)
        )

    def get_all_users(self):
        users = self.user_service.get_all_users()
        return api_response(data=users)

    def create_new_user(self):
        data = request.json
        user_creation  = self.user_create_request.load(data)
        response = self.user_service.create_new_user(user_creation)
        return api_response(
            status=True,
            message="User created successfully",
            data=response,
            status_code=201
        )

    def get_user_detail(self, user_id):
        response = self.user_service.get_user_detail(user_id)
        return api_response(data=response) 


user_controller = UserController()
user_bp = user_controller.user_bp
