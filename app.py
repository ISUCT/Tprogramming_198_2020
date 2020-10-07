from flask import Flask
app = Flask(__name__)
import datetime
from flask import render_template
import dog
import dog as Dog

collection = []
def init():
    dog1 = dog.Dog("Leo")
    collection.append(dog1)
    dog2 = dog.Dog("Yuuki")
    collection.append(dog2)
    dog3 = dog.Dog("Lisa)
    collection.append(dog3)

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

@app.route("/dogs/new", methods=["GET", "POST"])
def dogs_add():
    name = request.form.get("name", default="", type=str)
    age = request.form.get("age", default="0", type=float)
    if name:
       dog1 = dog.Dog(name)
        dog1.age = age
        collection.append(dog1)
    return render_template("new.html")

@app.route('/dogs/<name>')
def dog(name):
    item = None
    for el in collection:
        if name == el.name:
            item = el
            break

    return render_template(dog.html", item=item)

@app.route('/dogs')
def rabbits():
    return render_template ("dogs.html", collection = collection)