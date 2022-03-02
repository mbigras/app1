import os

import flask

app = flask.Flask(__name__)
app.config["version"] = __version__ = "0.0.1"
app.config["env"] = os.environ.get("ENV", "dev")
app.config["default_settings"] = {
    "foo": "default foo",
    "bar": "default bar",
    "baz": "default baz",
}
app.config["settings"] = {
    "foo": os.environ.get("FOO", app.config["default_settings"]["foo"]),
    "bar": os.environ.get("BAR", app.config["default_settings"]["bar"]),
    "baz": os.environ.get("BAZ", app.config["default_settings"]["baz"]),
}


@app.route("/")
def hello():
    return flask.jsonify(
        app=app.name,
        env=app.config["env"],
        version=app.config["version"],
        settings=app.config["settings"],
    )
