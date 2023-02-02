from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def landing():
    return """
        <h1>Go to /welcome/home, /welcome/back, or /home</h1>
    """

@app.route('/welcome')
def welcome():
    return "welcome"

@app.route('/welcome/home')
def home():
    return 'welcome home'

@app.route('/welcome/back')
def welcome_back():
    return 'welcome back'