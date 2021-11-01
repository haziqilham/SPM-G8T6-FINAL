import flask
import time

app = flask.Flask(__name__)


@app.route("/")
def index():
    return "PUSHED AT 11:40 ", time.localtime
