import flask
from auth import auth
from dbclient import Collection, Document
from utils import login_required

app = flask.Flask(__name__)
app.secret_key = 'secret'

db = Collection('db')

@app.route('/')
def landing():
    if 'id' in flask.session:
        return flask.redirect(flask.url_for('dashboard'))
    return flask.render_template('landing.html')

@app.route('/dashboard')
@login_required
def dashboard():
    user = db['users'][flask.session['id']]
    return flask.render_template('dashboard.html', user=user)

app.register_blueprint(auth)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
