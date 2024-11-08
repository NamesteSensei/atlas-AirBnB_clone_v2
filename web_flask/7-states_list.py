#!/usr/bin/python3
"""Flask web application to display list of all State objects in storage"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """Renders HTML with list of states sorted by name"""
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def close_storage(exc):
    """Close the current SQLAlchemy session after request"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
