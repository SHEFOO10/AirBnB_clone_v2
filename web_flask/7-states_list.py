#!/usr/bin/python3
""" List of states Flask script """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list',
           strict_slashes=False)
def list_states():
    """ list states """
    states = storage.all(State)
    filtered_states = []
    for state, state_obj in states.items():
        filtered_states.append((state_obj.id, state_obj.name))
    return render_template('7-states_list.html', states=filtered_states)


@app.teardown_appcontext
def teardown_db(exception=None):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
