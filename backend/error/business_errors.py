class BusinessError(Exception):
    """Lớp cha cho tất cả các lỗi business logic."""
    status_code = 400  # Mặc định lỗi business là 400 Bad Request

    def __init__(self, message="Business logic error", status_code=None):
        super().__init__(message)
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        """Chuyển lỗi thành dict để trả về JSON."""
        return {
            "error": self.__class__.__name__,
            "message": self.message,
            "status_code": self.status_code
        }


# 🎯 Các lỗi business cụ thể

class UserAlreadyExists(BusinessError):
    """Lỗi khi tạo user với username đã tồn tại."""
    def __init__(self):
        super().__init__("User already exists", 409)

class InsufficientBalance(BusinessError):
    """Lỗi khi user không đủ tiền để thực hiện giao dịch."""
    def __init__(self):
        super().__init__("Insufficient balance", 402)

class UnauthorizedAction(BusinessError):
    """Lỗi khi user không có quyền thực hiện hành động này."""
    def __init__(self):
        super().__init__("You are not authorized to perform this action", 403)

class ComponentNotFound(BusinessError):
    """Lỗi khi component không tồn tại."""
    def __init__(self):
        super().__init__("Component not found", 404)

class ComponentDetailNotFound(BusinessError):
    """Lỗi khi component detail không tồn tại."""
    def __init__(self):
        super().__init__("Component detail not found", 404)

class CategoryNotFound(BusinessError):
    """Lỗi khi category không tồn tại."""
    def __init__(self):
        super().__init__("Category not found", 404)

class DeviceNotFound(BusinessError):
    """Lỗi khi device không tồn tại."""
    def __init__(self):
        super().__init__("Device not found", 404)

class DeviceDetailNotFound(BusinessError):
    """Lỗi khi device detail không tồn tại."""
    def __init__(self):
        super().__init__("Device detail not found", 404)

class DeviceAlreadyExists(BusinessError):
    """Lỗi khi device đã tồn tại."""
    def __init__(self):
        super().__init__("Device already exists", 409)

class RefreshTokenNotFound(BusinessError):
    """Lỗi khi refresh token không tồn tại."""
    def __init__(self):
        super().__init__("Refresh token not found", 404)

