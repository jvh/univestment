from flask import Flask, jsonify, request
from flask_restful.utils.cors import crossdomain
from flask_cors import CORS
from back_end.src import import_files as imp
from back_end.src import DEVELOPMENT

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/test_data', methods=['GET', 'POST'])
@crossdomain(origin='*')
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
    print(data.trends())

    return 'test'


class DataManipulation:
    def trends(self):
        files = imp.ImportFiles()
        return files.box_office_data


data = DataManipulation()

if __name__ == '__main__':
    # print(data.trends())
    if DEVELOPMENT:
        app.run(port=5000, debug=True)
    else:
        app.run(port=5000, debug=False)
