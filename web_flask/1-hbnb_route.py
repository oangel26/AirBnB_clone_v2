#!/usr/bin/python3
"""
Script that starts a Flask web application:
* /: display “Hello HBNB!”
* /hbnb: display “HBNB”
"""


from flask import Flask


app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def say_hello():
    """ Function that returns greetings """
    return "Hello HBNB!"


@app.route('/hbnb', methods=['GET'], strict_slashes=False)
def say_HBNB():
    """ Function that returns greetings """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
