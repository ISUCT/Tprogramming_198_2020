from flask import Flask
app = Flask(__name__)
import datetime
from flask import render_template
import rabbit
import rabbit as Rabbit

collection = []
def init():
    rabbit1 = rabbit.Rabbit("Nemo")
    collection.append(rabbit1)
    rabbit2 = rabbit.Rabbit("Dori")
    collection.append(rabbit2)
    rabbit3 = rabbit.Rabbit("SwordRabbit")
    collection.append(rabbit3)

init()
@app.route('/')
def hello_world():
    return f'Hello, World! {datetime.datetime.now()}'

@app.route('/test')
def test():
    user = {'username': 'Miguel'}
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

@app.route("/rabbits/new", methods=["GET", "POST"])
def rebbits_add():
    name = request.form.get("name", default="", type=str)
    age = request.form.get("age", default="0", type=float)
    if name:
        rabbit1 = rabbit.Rabbit(name)
        rabbit1.age = age
        collection.append(rabbit1)
    return render_template("new.html")

@app.route('/rabbits/<name>')
def rebbit(name):
    item = None
    for el in collection:
        if name == el.name:
            item = el
            break
    
    return render_template("rabbit.html", item=item)

@app.route('/rabbits')
def rabbits():
    return render_template ("rebbits.html", collection = collection)






    