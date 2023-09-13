from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def tip_calculator():
    if request.method == "POST":
        total = float(request.form["total"])
        tip = int(request.form["tip"])
        people = int(request.form["people"])

        total_pay = total + total * (tip / 100)
        each_bill = round(total_pay / people)
        return render_template("result.html", each_bill=each_bill)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8891)
