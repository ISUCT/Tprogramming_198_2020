from flask import Flask
app = Flask(__name__)
import datetime


@app.route('/')
def hello_world():
    return f'Hello, World! {datetime.datetime.now()}'