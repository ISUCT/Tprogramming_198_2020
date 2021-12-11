from flask import Flask
app = Flask(__name__)
import datetime

@app.route('/')
def hello_world():
    return f'<h1>Hello 1 </h1>, World! Prog {datetime.datetime.now()} '