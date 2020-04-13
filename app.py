from flask import Flask
app = Flask(__name__)
import datetime
from flask import render_template


@app.route('/')
def hello_world():
    return f'Hello 1, World! {datetime.datetime.now()}'

@app.route('/test')
def test():
    user = {'username': 'Eugeny'}
    return render_template('index.html', title='Home', user=user)

from flask import request

@app.route('/params')
def params():
    print(request.args)
    a = request.args.get("a", default=0, type=float)
    b = request.args.get("b", default=0, type=float)
    return f'Hello {a} + {b} = {a + b}'
    # http://127.0.0.1:5000/params?a=5&b=8

@app.route('/calc', methods=['GET', 'POST'])
def calc():
    a = request.form.get("a", default=0, type=float)
    b = request.form.get("b", default=0, type=float)
    summ = a + b
    return render_template('calc.html', result=summ)
