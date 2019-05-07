from flask import Flask, jsonify

DEBUGGING_MODE = True

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/test_data', methods=['GET', 'POST'])
def test_data():
    return jsonify({'result': {'data': [1, 2, 3, 4, 5, 9, 10, 7, 8]}})


if __name__ == '__main__':
    app.run(port=5000, debug=DEBUGGING_MODE)
