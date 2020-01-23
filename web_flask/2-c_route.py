#!/usr/bin/python3
"""
    start flask
"""


from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def root():
    """ test """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ test """
    return "HBNB"


@app.route("/c/<balls>", strict_slashes=False)
def c_my(balls):
    """ display text """
    return "C "+balls.replace("_", " ")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
