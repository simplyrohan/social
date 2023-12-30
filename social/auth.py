import flask

auth = flask.Blueprint("auth", __name__, url_prefix="/auth")


@auth.route("/signin", methods=["GET", "POST"])
def login():
    if flask.request.method == "GET":
        return flask.render_template("auth/signin.html")


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if flask.request.method == "GET":
        return flask.render_template("auth/signup.html")
    else:
        username, password = flask.request.form["username"], flask.request.form["password"]
        
        