#!/usr/bin/python3
"""
This script starts a Flask web application that listens on 0.0.0.0, port 5000.
The root route ("/") displays "Hello HBNB!".
The "/hbnb" route displays "HBNB".
The "/c/<text>" route displays "C " followed by the value of the text variable (with underscores replaced by spaces).
"""
from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Displays 'C ' followed by the value of the text variable, with underscores replaced by spaces"""
    text = escape(text).replace('_', ' ')
    return f"C {text}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
