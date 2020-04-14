from flask import Flask
app = Flask(__name__)
import datetime
from flask import render_template
import pig as Pig

collection = []
def init():
    pig1 = Pig.Pig("Rita")
    collection.append(pig1)
    pig2 = Pig.Pig("Rata")
    collection.append(pig2)
    pig3 = Pig.Pig("bigPig")
    collection.append(pig3)

init()


@app.route('/')
def hello_world():
    return f'Hello 1, World! {datetime.datetime.now()}'

@app.route('/test')
def test():
    user = {'username': 'Natasha'}
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
        sign = "X"
    return render_template('calc.html', result=res, sign=sign)

@app.route("/pigs")
def pigs():
    return render_template("pigs.html", collection=collection)

from flask import redirect
@app.route("/pigs/new", methods=["GET", "POST"])
def pig_add():
    print("Test")
    name = request.form.get("name", default="", type=str)
    age = request.form.get("age", default=0, type=float)
    if name:
        print("Got Name")
        pig = Pig.Pig(name)
        pig.age = age
        collection.append(pig)
        return redirect("/pigs")
    return render_template("new.html")

@app.route("/pigs/<name>")
def pig(name):
    item = None
    for el in collection:
        if name == el.name:
            item = el
            break
    return render_template("pig.html", item=item)