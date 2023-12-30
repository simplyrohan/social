import flask
from auth import auth
app = flask.Flask(__name__)

@app.route('/')
def landing():
    return flask.render_template('landing.html')

app.register_blueprint(auth)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)