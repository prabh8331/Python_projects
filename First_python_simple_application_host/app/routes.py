from app import app
from flask import request, render_template

@app.route("/", methods=["GET", "POST"])
def concatenate():
    result = ""
    if request.method == "POST":
        value1 = request.form["value1"]
        value2 = request.form["value2"]
        result = value1 + value2
    return render_template("index.html", result=result)
