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
            flask.session.pop('id')
            return flask.redirect(flask.url_for('landing'))
        
        return f(*args, **kwargs)
    return decorated_function

def get_user(uid=None, username=None):
    if uid:
        return db['users'][uid]
    elif username:
        return db['users'].query(lambda x: x['username'] == username)[0]
    