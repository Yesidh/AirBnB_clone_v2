#!/usr/bin/python3
# script that starts a Flask web application:
# Your web application must be listening on 0.0.0.0, port 5000
# Routes:
#        /: display “Hello HBNB!”
#        /hbnb: display "HBNB"
#        /c/<text>: display "C" followed tye the value of the text

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """function that return Hello HBNB"""

    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """function that return HBNB"""

    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """function that return c <text>"""

    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """function that return Python <text>"""

    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """function that return n if it's intege"""

    if isinstance(n, int):
        return '{} is a number'.format(n)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
