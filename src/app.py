import sys

from flask import Flask

from src.middlewares import request_middleware
from src.routes import bp

app = Flask(__name__)
app.logger.setLevel("INFO")
app.register_blueprint(bp)

request_middleware(app)


def main() -> None:
    debug = "--debug" in sys.argv
    app.run(host="0.0.0.0", port=5000, debug=debug)
