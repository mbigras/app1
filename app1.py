import flask

app = flask.Flask(__name__)
app.config["VERSION"] = "0.0.1"


@app.route("/")
def up():
    config = app.config
    config["PERMANENT_SESSION_LIFETIME"] = str(config["PERMANENT_SESSION_LIFETIME"])
    config["SEND_FILE_MAX_AGE_DEFAULT"] = str(config["SEND_FILE_MAX_AGE_DEFAULT"])
    return flask.jsonify(config)
