#!/usr/bin/python3

"""a script that starts a Flask web application"""

from flask import Flask, render_template

app = Flask(__name__)

# route page


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"

# hbnb page


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"

# <text> page


@app.route("/c/<text>", strict_slashes=False)
def show_text(text):
    s = ""
    for i in text:
        s += i if i != "_" else " "
    return f"C {s}"

# <text> with default page


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    return f"Python {text.replace('_', ' ')}"

# number page


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    return f"{n} is a number"

# template page 1


@app.route("/number_template/<int:n>", strict_slashes=False)
def template(n):
    return render_template("5-number.html", n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
