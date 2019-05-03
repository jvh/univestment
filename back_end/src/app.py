from flask import Flask

DEBUGGING_MODE = True

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(port=5000, debug=DEBUGGING_MODE)
