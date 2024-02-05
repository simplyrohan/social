import flask
import os
from utils import get_user, login_required

profile = flask.Blueprint("profile", __name__, url_prefix="/profile")


@profile.route("/<username>", methods=["GET", "POST"])
@login_required
def profile_view(username):
    if flask.request.method == "GET":
        user = get_user(uid=flask.session["id"])
        profile = get_user(username=username)
        return flask.render_template(
            "profile.html",
            user=user,
            profile=profile,
            editable=(user["id"] == profile["id"]),
        )
    elif flask.request.method == "POST":
        # PFP change
        user = get_user(uid=flask.session["id"])
        profile = get_user(username=username)

        if user["id"] == profile["id"]:
            if "pfp" not in flask.request.files:
                return flask.redirect("/")
            
            file = flask.request.files["pfp"]
            file.save(os.path.join('social/static/generated', user['id']+os.path.splitext(file.filename)[1]))
            user['picture'] = user['id']+os.path.splitext(file.filename)[1]
        return flask.redirect("/dashboard")
