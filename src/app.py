import flask
import time

app = flask.Flask(__name__)


@app.route("/")
def index():
<<<<<<< Updated upstream
    return "Welcome!!! ", time.localtime
=======
    return "Welcome!!sssss", time.localtime
>>>>>>> Stashed changes
