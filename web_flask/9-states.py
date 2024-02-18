#!/usr/bin/python3
""" List of states Flask script """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>',
           strict_slashes=False)
def list_states(id=None):
    """ list states """
    states = storage.all(State)
    sorted_states = sorted(list(states.values()), key=lambda state: state.name)
    try:
        state = states['State.' + id] if id is not None else None
    except (KeyError):
        state = None
        sorted_states = None
    return render_template('9-states.html', states=sorted_states, state=state)


@app.teardown_appcontext
def teardown_db(exception=None):
    """ refresh database after every request """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
