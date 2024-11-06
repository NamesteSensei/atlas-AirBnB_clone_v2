# main_0.py
# Testing states creation with a name provided

from models import storage
from models.state import State

print("All states before adding new ones:", len(storage.all(State)))

# Ensure the State instance is initialized with a name
new_state = State(name="California")  
new_state.save()

print("All states after adding a new one:", len(storage.all(State)))
