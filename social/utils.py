import flask
import dbclient
from functools import wraps

db = dbclient.Collection('db')

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'id' not in flask.session:
            return flask.redirect(flask.url_for('landing'))
        if not db['users'].query(lambda x: x['id'] == flask.session['id']):
            return flask.redirect(flask.url_for('landing'))
        return f(*args, **kwargs)
    return decorated_function