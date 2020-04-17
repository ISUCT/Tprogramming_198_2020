from flask import Flask
app = Flask(__name__)
import datetime
from flask import render_template
import tv as Tv

collection = []
def init():
    tv1 = TV.TV("samsung")
    collection.append(tv1)
    tv2 = TV.TV("LD")
    collection.append(tv2)
    tv3 = TV.TV("Philips")
    collection.append(tv3)

    init()

@app.route('/')
def hello_world():
    return f'Hello 1, World! {datetime.datetime.now()}'

@app.route('/')
def test():
    user = {'username': 'Lidia'}
    return render_template('index.html', title='Home', user=user)

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

@app.route("/TV/new", methods=["GET", "POST"])
def tv_add():
    name = request.form.get("name", default = "")