#!/usr/bin/python3
"""
Script that starts a Flask web application:
* /: display “Hello HBNB!”
* /hbnb: display “HBNB”
* /c/<text>: display “C ” followed by the value of the text \
variable (replace underscore _ symbols with a space)
* /python/(<text>): display “Python ”, followed by the value of the text \
variable (replace underscore _ symbols with a space )
* /number/<n>: display “n is a number” only if n is an integer
* /number_template/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n” inside the tag BODY
* /number_odd_or_even/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n is even|odd” inside the tag BODY
"""


from flask import Flask, abort, render_template
import re

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


@app.route('/number/<n>', methods=['GET'], strict_slashes=False)
def is_number(n):
    """ Function that display “n is a number ” only if is an integer
    """
    result = re.match("[-+]?\d+$", n)
    if result:
        return "{} is a number".format(n)
    else:
        return abort(404)


@app.route('/number_template/<n>', methods=['GET'], strict_slashes=False)
def display_html(n):
    """ display a HTML page only if n is an integer:
    H1 tag: “Number: n” inside the tag BODY
    """
    result = re.match("[-+]?\d+$", n)
    if result:
        context = {
            'n': n,
        }
        return render_template("5-number.html", **context)
    else:
        return abort(404)


@app.route('/number_odd_or_even/<n>', methods=['GET'], strict_slashes=False)
def display_odd_or_even(n):
    """ display a HTML page only if n is an integer:
    H1 tag: “Number: n is even|odd” inside the tag BODY
    """
    result = re.match("[-+]?\d+$", n)
    if result:
        if int(n) % 2 == 0:
            odd_or_even = "even"
        else:
            odd_or_even = "odd"
        context = {
            'n': n,
            'odd_or_even': odd_or_even,
        }
        return render_template("6-number_odd_or_even.html", **context)
    else:
        return abort(404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
