from flask import Flask, render_template, request
from pymongo import MongoClient
app = Flask(__name__)
my_client = MongoClient("localhost", 27017)
my_db = my_client["calci"] # database
results = my_db["results"] # collection

@app.route("/", methods=["GET", "POST"])
def homePage():
    if request.method == "POST":
        n1 = int(request.form["num1"])
        operation = request.form["operation"]
        n2 = int(request.form["num2"])
        if operation == "add":
            res = f"{n1} + {n2} is {n1+n2}"
            results.insert_one({
                "number1":n1, "number2":n2, "operator":operation, "output":res
            })
            return render_template("index.html", output=res)
        elif operation == "sub":
            res = f"{n1} - {n2} is {n1-n2}"
            results.insert_one({
                "number1":n1, "number2":n2, "operator":operation, "output":res
            })
            return render_template("index.html", output=res)
        elif operation == "mul":
            res = f"{n1} x {n2} is {n1*n2}"
            results.insert_one({
                "number1":n1, "number2":n2, "operator":operation, "output":res
            })
            return render_template("index.html", output=res)
        elif operation == "div":
            try:
                res = f"{n1} / {n2} is {n1/n2}"
                results.insert_one({
                "number1":n1, "number2":n2, "operator":operation, "output":res
                 })
                return render_template("index.html", output=res)
            except Exception as e:
                error = "Please change num2 as non-zero"
                return render_template("index.html", output=error)
        
    else:
        return render_template("index.html")
app.run(debug=True)