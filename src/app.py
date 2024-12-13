import sys

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


def main() -> None:
    debug = '--debug' in sys.argv
    app.run(host="0.0.0.0", port=5000, debug=debug)
