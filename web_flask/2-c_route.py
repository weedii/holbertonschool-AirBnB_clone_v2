#!/usr/bin/python3

"""a script that starts a Flask web application"""

from flask import Flask

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


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
