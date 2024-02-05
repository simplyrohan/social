import flask
from auth import auth
from profile import profile
from dbclient import Collection, Document
from utils import login_required, get_user
import os

for filename in os.listdir('social/static/sass'):
    if filename.endswith('.scss'):
        os.system(f'sass social/static/sass/{filename} social/static/styles/{filename.replace(".scss", ".css")}')

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
    user = get_user(uid=flask.session['id'])
    return flask.render_template('dashboard.html', user=user)

app.register_blueprint(auth)
app.register_blueprint(profile)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
