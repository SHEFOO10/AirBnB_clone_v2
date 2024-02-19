#!/usr/bin/python3
""" Hbnb filters with Flask Server """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)


@app.route('/hbnb',
           strict_slashes=False)
def hbnb_filters():
    """ hbnb_filters """
    states = storage.all(State)
    sorted_states = sorted(list(states.values()),
                           key=lambda state: state.name)
    amenities = sorted(list(storage.all(Amenity).values()),
                       key=lambda amenity: amenity.name)
    places = sorted(list(storage.all(Place).values()),
                    key=lambda place: place.name)
    return render_template('100-hbnb.html',
                           states=sorted_states,
                           amenities=amenities,
                           places=places)


@app.teardown_appcontext
def teardown_db(exception=None):
    """ refresh database after every request """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
