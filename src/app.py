import flask
import time

app = flask.Flask(__name__)


@app.route("/")
def index():
    return "Welcome!!11:aaa41sssss", time.localtime
