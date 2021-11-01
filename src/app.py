import flask
import time

app = flask.Flask(__name__)


@app.route("/")
def index():
    return "Welcome!!1!!!1:4aaaa1ss!!!sss", time.localtime
