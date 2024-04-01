# import html # html_code.escape() is used to thwart XSS attacks
import flask
import os
import datetime
import scanner

# ----------------------------------------------------------------------

app = flask.Flask(__name__, template_folder="./templates")


# ----------------------------------------------------------------------

@app.route("/", methods=["GET"])
def index():
    # render homepage html 
    html_code = flask.render_template("index.html")
    response = flask.make_response(html_code)

    return response

@app.route("/scan", methods=["GET"])
def scan():
    # get address from app
    address = flask.request.args.get("address")

    # get contract_code
    contract_code = scanner.get_contract_code(address)

    # analyse with GPT

    return  
