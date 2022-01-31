#!/usr/bin/python3
"""
Script that starts a Flask web application:
* /: display “Hello HBNB!”
* /hbnb: display “HBNB”
* /c/<text>: display “C ” followed by the value of the text \
variable (replace underscore _ symbols with a space)
* /python/(<text>): display “Python ”, followed by the value of the text \
variable (replace underscore _ symbols with a space )
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


@app.route('/c/<text>', methods=['GET'], strict_slashes=False)
def c_is_fun(text=None):
    """ Function that display “C ” followed by
    the value of the text variable
    """
    new_text = text.replace('_', ' ')
    return "C {}".format(new_text)


@app.route('/python/<text>', methods=['GET'], strict_slashes=False)
@app.route('/python/', methods=['GET'], strict_slashes=False)
def python_is_cool(text="is cool"):
    """ Function that display “Python ” followed by
    the value of the text variable
    """
    new_text = text.replace('_', ' ')
    return "Python {}".format(new_text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
