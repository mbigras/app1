import os
import socket

import flask

app = flask.Flask(os.environ.get("APP", "app1"))
app.config["org"] = os.environ.get("ORG", "unset")
app.config["owner"] = os.environ.get("OWNER", "unset")
app.config["env"] = os.environ.get("ENV", "unset")
app.config["features"] = os.environ.get("FEATURES", "unset")


@app.route("/")
def hello():
    return flask.jsonify(
        app=app.name,
        org=app.config["org"],
        owner=app.config["owner"],
        env=app.config["env"],
        features=app.config["features"],
        host=socket.gethostname(),
    )
