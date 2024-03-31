# import html # html_code.escape() is used to thwart XSS attacks
import flask
import os
import datetime

# ----------------------------------------------------------------------

app = flask.Flask(__name__, template_folder="./templates")


# ----------------------------------------------------------------------

@app.route("/", methods=["GET"])
def index():
    html_code = flask.render_template("index.html")
    response = flask.make_response(html_code)
    return response