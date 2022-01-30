#!/usr/bin/python3
""" Script that starts a Flask web application: """


from flask import Flask


app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def say_hello():
    """ Function that returns greetings """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
