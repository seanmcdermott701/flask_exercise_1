# Put your app in here.
from operations import add, sub, mult, div
from flask import Flask, request

app = Flask(__name__)

# Getting 1 error from the unit test although the app works fine

@app.route('/')
def landing():
    return """
    <h1>Visit /add, /sub, /mult, or /div with a and b as query params</h1>
    """

@app.route('/add')
def add_route():
    a = int(request.args['a'])
    b = int(request.args['b'])
    answer = str(add(a, b))
    return answer

@app.route('/sub')
def sub_route():
    a = int(request.args['a'])
    b = int(request.args['b'])
    answer = str(sub(a, b))
    return answer

@app.route('/mult')
def mult_route():
    a = int(request.args['a'])
    b = int(request.args['b'])
    answer = str(mult(a, b))
    return answer

@app.route('/div')
def div_route():
    a = int(request.args['a'])
    b = int(request.args['b'])
    answer = str(div(a, b))
    return answer