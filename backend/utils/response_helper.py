from flask import jsonify

def api_response(status=True, message="", data=None, status_code=200):
    response = {
        "status": "success" if status else "failed",
        "message": message,
        "data": data,
        "status_code": status_code
    }
    return jsonify(response), status_code
