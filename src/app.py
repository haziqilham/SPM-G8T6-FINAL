import flask
import time

app = flask.Flask(__name__)


@app.route("/")
def index():
    return "Welcome!!1!!!1:41ss!!!sss", time.localtime
