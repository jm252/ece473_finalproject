# import html # html_code.escape() is used to thwart XSS attacks
import flask
import os
import datetime
import scanner
import analysis

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
    print(address)

    # get contract code
    contract_code = scanner.get_contract_code(address)

    # get contract analysis 
    contract_summary = analysis.smart_contract_summary(contract_code)
    print(contract_summary)
    contract_class = analysis.smart_contract_class(contract_code)
    print(contract_class)

    html_code = flask.render_template("scan.html", 
                                            contract_class = contract_class, 
                                            contract_summary=contract_summary)
    response = flask.make_response(html_code)
    
    return response 
