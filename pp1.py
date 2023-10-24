import flask

app = flask.Flask(__name__)


@app.route('/api/v1/hello-world-1', methods=['GET'])
def hello_world():
    response_data = "Hello World 1"
    return flask.jsonify(response_data), 200


if __name__ == '__main__':
    app.run()
