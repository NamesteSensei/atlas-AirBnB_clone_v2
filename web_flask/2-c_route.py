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
    """Displays 'C ' followed by the value of <text>
    Replaces underscores in <text> with spaces."""
    # Replace underscores in the text with spaces
    formatted_text = text.replace('_', ' ')
    # Return the formatted string with "C " prefix
    return f"C {formatted_text}"


# Run the application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
