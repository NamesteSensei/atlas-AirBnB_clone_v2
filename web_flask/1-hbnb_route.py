#!/usr/bin/python3
"""A Flask web application with two routes"""

from flask import Flask

# Initialize the Flask application
app = Flask(__name__)


# Route for the root URL
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!' when accessing the root URL"""
    return "Hello HBNB!"


# Route for /hbnb
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB' when accessing /hbnb"""
    return "HBNB"


# Run the application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
