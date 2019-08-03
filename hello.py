"""Flask app router"""

import flask
import randomfact

APP = flask.Flask(__name__)

@APP.route('/')
def hello_world():
    """Basic root page"""
    return 'Hello, World!'

@APP.route('/pandafacts')
def panda_facts():
    """Display random facts about pandas"""
    return randomfact.randomfact("pandafacts.txt")

@APP.route('/pandagif')
def panda_gif():
    """Display gif of a panda"""
    return APP.send_static_file('panda.gif')

if __name__ == '__main__':
    APP.run(debug=True, host='0.0.0.0')
