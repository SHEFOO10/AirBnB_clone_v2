#!/usr/bin/python3
""" List of states Flask script """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters',
           strict_slashes=False)
def list_states():
    """ list states """
    states = storage.all(State)
    sorted_states = sorted(list(states.values()),
                           key=lambda state: state.name)
    amenities = sorted(list(storage.all(Amenity).values()),
                       key=lambda amenity: amenity.name)
    return render_template('10-hbnb_filters.html',
                           states=sorted_states, amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception=None):
    """ refresh database after every request """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
