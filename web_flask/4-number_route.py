#!/usr/bin/python3
"""A Flask web application with multiple routes"""

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


# Dynamic route for /c/<text>
@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Displays 'C ' followed by the value of <text>, with underscores
    replaced by spaces."""
    formatted_text = text.replace('_', ' ')
    return f"C {formatted_text}"


# Dynamic route for /python/<text> with a default value
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    """Displays 'Python ' followed by the value of <text>. Replaces
    underscores in <text> with spaces. Defaults to 'is cool' if <text>
    is not provided."""
    formatted_text = text.replace('_', ' ')
    return f"Python {formatted_text}"


# Route for /number/<n> that only accepts integers
@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Displays '<n> is a number' if n is an integer"""
    return f"{n} is a number"


# Run the application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
