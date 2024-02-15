#!/usr/bin/python3
""" Initiate Flask Server """
from flask import Flask
app = Flask(__name__)


@app.route("/",
           strict_slashes=False)
def hello_world():
    """ handle route to index"""
    return "Hello HBNB!"


@app.route("/hbnb",
           strict_slashes=False)
def hbnb():
    """ handle route to /hbnb """
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
