#!/usr/bin/python3
from flask import Flask, render_template, request, redirect,session

app = Flask(__name__)
app.config["SECRET_KEY"] = '2j34jb123kj51kj6kj1324kj1l25h32'

groups = [{"hostname": "hostA","ip": "192.168.30.22", "fqdn": "hostA.localdomain"},
          {"hostname": "hostB", "ip": "192.168.30.33", "fqdn": "hostB.localdomain"},
          {"hostname": "hostC", "ip": "192.168.30.44", "fqdn": "hostC.localdomain"}]

@app.route("/")
def index():
    if "allowed" in session:
        login = "allowed"
    else:
        login = "no"
    return render_template("network.html", groups=groups, login=login)

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/login/<name>")
def login(name):
    session["allowed"] = name
    return redirect("/")

@app.route("/logout")
def logout():
    session.pop("allowed", None)
    return redirect("/")

@app.route("/addnew", methods=["POST"])
def new():
    hostname = request.form.get("hostname")
    ip = request.form.get("ip")
    fqdn = request.form.get("fqdn")
    groups.append({"hostname": hostname, "ip": ip, "fqdn": fqdn})
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
