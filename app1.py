import os
import socket

import flask

app = flask.Flask(os.environ.get("APP", "app1"))
app.config["image"] = os.environ.get("IMAGE", "unset")
app.config["org"] = os.environ.get("ORG", "unset")
app.config["owner"] = os.environ.get("OWNER", "unset")
app.config["env"] = os.environ.get("ENV", "unset")
app.config["features"] = os.environ.get("FEATURES", "unset")
app.config["JSON_SORT_KEYS"] = False
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True

@app.route("/")
def hello():
    return flask.jsonify(
        app=app.name,
        image=app.config["image"],
        org=app.config["org"],
        owner=app.config["owner"],
        env=app.config["env"],
        features=app.config["features"],
        host=socket.gethostname(),
    )
