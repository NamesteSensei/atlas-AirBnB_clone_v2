#!/usr/bin/python3
"""A Flask web application with two routes"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route for the root URL, displays 'Hello HBNB!'"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route for /hbnb, displays 'HBNB'"""
    return "HBNB"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
