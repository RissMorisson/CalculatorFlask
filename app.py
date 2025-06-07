from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operation = request.form["operation"]

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Error: Cannot divide by zero!"
            else:
                result = "Invalid operation!"
        except ValueError:
            result = "Please enter valid numbers!"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
