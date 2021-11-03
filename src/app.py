<<<<<<< HEAD
<<<<<<< HEAD
import flask, time
=======
import flask
import time
>>>>>>> Claudia
=======
import flask
import time
>>>>>>> Marcus

app = flask.Flask(__name__)


@app.route("/")
def index():
<<<<<<< HEAD
<<<<<<< HEAD
    return "Welcome!!! ",time.localtime
=======
    return "PUSHED AT 11:40 ", time.localtime
>>>>>>> Claudia
=======
    return "Welcome!!1!!!1:4aaaa1ss!!!sss", time.localtime
>>>>>>> Marcus
