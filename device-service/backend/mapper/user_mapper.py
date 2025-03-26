from backend.entities.user import User
from backend.dto.response.user.user_reponse import UserResponseSchema

class UserMapper:
    def __init__(self):
        self.user_response_schema = UserResponseSchema()

    def to_user_response(self, user: User):
        """Chuyển đối tượng User thành UserResponse chuẩn hóa."""
        user_data = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "country_id": user.country_id
        }
        return self.user_response_schema.dump(user_data)
