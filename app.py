from flask import Flask
app = Flask(__name__)
from flask import render_template


@app.route('/')
def hello_world():
    return f'Hello 1, World! {datetime.datetime.now()}'     

from flask import request

@app.route('/params')
def params():
    print(request.args)
    a = request.args.get("a", default=0, type=float)
    b = request.args.get("b", default=0, type=float)
    return f'Hello {a} + {b} = {a + b}'

@app.route('/calc/<type_calc>', methods=['GET', 'POST'])
def calc(type_calc):
    a = request.form.get("a", default=0, type=float)
    b = request.form.get("b", default=0, type=float)
    res = 0
    sign = ""
    if type_calc == "summ":
        res = a + b
        sign = "+"
    if type_calc == "mul":
        res = a*b
        sign = "x"
    return render_template('calc.html', result=res, sign=sign)