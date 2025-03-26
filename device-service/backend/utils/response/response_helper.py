from flask import jsonify
from dataclasses import asdict, is_dataclass

def api_response(status: bool = True, message: str = None, data=None, status_code: int = 200):
    """
    Chuẩn hóa response API trả về JSON.

    - Nếu `data` là một dataclass instance, chuyển thành dictionary.
    - Loại bỏ các trường có giá trị None để tối ưu response.
    """
    if is_dataclass(data) and not isinstance(data, type):
        data = asdict(data)

    response = {
        "status": "success" if status else "failed",
        "message": message,
        "data": data,
        "status_code": status_code
    }

    # Loại bỏ các trường có giá trị None
    filtered_response = {key: value for key, value in response.items() if value is not None}

    return jsonify(filtered_response), status_code
