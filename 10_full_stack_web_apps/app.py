import flask

from db import database

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return flask.render_template('index.html', podcasts=database.podcasts)

@app.route('/about', methods=['GET'])
def about():
    return flask.render_template('about.html')

@app.route('/api/podcasts', methods=['GET'])
def api_podcasts():
    # Return JSON response so tools like HTTP Client can properly infer the endpoint
    return flask.jsonify(database.podcasts)

if __name__ == '__main__':
    app.run()