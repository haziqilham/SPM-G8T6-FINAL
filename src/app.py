<<<<<<< HEAD
import flask, time
=======
import flask
import time
>>>>>>> Claudia

app = flask.Flask(__name__)


@app.route("/")
def index():
<<<<<<< HEAD
    return "Welcome!!! ",time.localtime
=======
    return "PUSHED AT 11:40 ", time.localtime
>>>>>>> Claudia
