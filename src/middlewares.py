from flask import current_app, request, Flask, Response


def log_request() -> None:
    request_dict = {
        "headers": request.headers,
        "data": request.get_data(as_text=True),
        "path": request.path,
        "method": request.method,
    }
    current_app.logger.info(f"Received request: {request_dict}")


def log_response(response) -> Response:
    response_dict = {
        "status_code": response.status_code,
        "data": response.data,
        "path": request.path,
        "method": request.method,
    }
    current_app.logger.info(f"Response: {response_dict}")
    return response


def request_middleware(app: Flask) -> None:
    app.before_request(log_request)
    app.after_request(log_response)
