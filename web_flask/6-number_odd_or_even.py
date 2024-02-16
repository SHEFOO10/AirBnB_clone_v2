#!/usr/bin/python3
""" Initiate Flask Server """
from flask import Flask, render_template
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


@app.route('/c/<text>',
           strict_slashes=False)
def get_text(text):
    return "C " + text.replace('_', ' ')


@app.route('/python/',
           strict_slashes=False)
@app.route('/python/<text>',
           strict_slashes=False)
def get_text_2(text="is cool"):
    """ get text from route /python/<text> """
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>',
           strict_slashes=False)
def get_int(n):
    return str(n) + " is a number"


@app.route('/number_template/<int:n>')
def number_template(n):
    """ return html template with the given number """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """ return even or odd based on the given number """
    even_or_odd = ('odd' if (n % 2) else 'even')
    return render_template('6-number_odd_or_even.html', n=n, type=even_or_odd)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
