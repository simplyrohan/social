import flask
import uuid
from dbclient import Collection, Document

auth = flask.Blueprint("auth", __name__, url_prefix="/auth")

db = Collection("db")


@auth.route("/signin", methods=["GET", "POST"])
def login():
    if flask.request.method == "GET":
        # print(flask.get_flashed_messages("error"))
        return flask.render_template(
            "auth/signin.html", msgs=flask.get_flashed_messages("error")
        )
    else:
        username, password = (
            flask.request.form["username"],
            flask.request.form["password"],
        )
        if not db["users"].query(lambda x: x["username"] == username):
            flask.flash("User not found", "error")
            return flask.redirect("/auth/signin")
        if not db["users"].query(lambda x: x["password"] == password):
            flask.flash("Incorrect password", "error")
            return flask.redirect("/auth/signin")
        
        # print(username, password)

        flask.session["id"] = db["users"].query(lambda x: x["username"] == username)[0]["id"]
        return flask.redirect(flask.url_for("dashboard"))



@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if flask.request.method == "GET":
        # print(flask.get_flashed_messages("error"))
        return flask.render_template(
            "auth/signup.html", msgs=flask.get_flashed_messages("error")
        )
    else:
        username, password = (
            flask.request.form["username"],
            flask.request.form["password"],
        )

        if db["users"].query(lambda x: x["username"] == username):
            flask.flash("Username already taken", "error")
            return flask.redirect("/auth/signup")

        # print(username, password)

        uid = uuid.uuid4().hex
        db["users"][uid] = {"id": uid, "username": username, "password": password, "picture": "0.svg"}

        flask.session["id"] = uid
        return flask.redirect(flask.url_for("dashboard"))
