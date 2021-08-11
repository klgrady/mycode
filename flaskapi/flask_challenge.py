#!/usr/bin/python3
from flask import Flask
from flask import redirect
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/")
@app.route("/wrongo")
def start():
    rule = request.url_rule
    if 'wrongo' in rule.rule:
        return render_template("trivia2.html")
    return render_template("trivia.html")

@app.route("/check", methods = ["POST"])
def answercheck():
    if request.json:
        input = request.json
        if input["answer"] == "C":
            redirect_url = "/correct"
    elif request.form.get("answer") == "C":
        redirect_url = "/correct"
    else:
        redirect_url = "/wrongo"
    return redirect(redirect_url)

@app.route("/correct")
def correct():
    return render_template("win.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
