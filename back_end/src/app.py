from flask import Flask, jsonify, request

DEBUGGING_MODE = True

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/test_data', methods=['GET', 'POST'])
def test_data():
    if request.method == 'POST':
        return 'ok'
    elif request.method == 'GET':
        return jsonify({'result': {'data': [1, 2, 3, 4, 5, 9, 10, 7, 8]}})


@app.route('/trend_data')
def trend_data():
    """
    Obtain the data for a set of movies and identify trends using time series analysis

    :return: The original data along with predicted data related to movie trends
    """
    return 'test'


if __name__ == '__main__':
    app.run(port=5000, debug=DEBUGGING_MODE)
