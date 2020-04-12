import flask
app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.send_from_directory('app/templates', 'index.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)