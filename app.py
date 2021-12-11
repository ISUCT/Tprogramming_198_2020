from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
import datetime
from flask import render_template
import Fish

collection = []
def init():
    fish1 = Fish.Fish("Nemo")
    collection.append(fish1)
    fish2 = Fish.Fish("Dori")
    collection.append(fish2)
    fish3 = Fish.Fish("SwordFish") 
    collection.append(fish3)

init()

@app.route('/')
def hello_world():
    return f'<h1>Hello 1 </h1>, World! Prog {datetime.datetime.now()}'

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

# http://127.0.0.1:5000/calc/summ
# http://localhost:5000/fishes/Dori
# http://localhost:5000/fishes/admnfg%20jdgjagd 

@app.route('/calc', methods=['GET', 'POST'])
def calc():
    a = request.form.get("a", default=0, type=float)
    b = request.form.get("b", default=0, type=float)
    res = 0
    sign = ""
    # if type_calc == "summ":
    res = a + b
    sign = "+"
    # if type_calc == "mul":
    #     res = a*b
    #     sign = "x"
    return render_template('calc.html', result=res, sign=sign)

@app.route("/fishes")
def fishes():
    print(collection)
    return render_template("fishes.html", collection=collection)

from flask import redirect
@app.route("/fishes/new", methods=["GET", "POST"])
def fish_add():
    print("Test")
    name = request.form.get("name", default="", type=str)
    age = request.form.get("age", default=0, type=float)
    if name:
        print("Got Name")
        fish = Fish.Fish(name)
        fish.age = age
        collection.append(fish)
        return redirect("/fishes")
    return render_template("new.html")

@app.route("/fishes/<name>")
def fish(name):
    item = None
    for el in collection:
        if name == el.name:
            item = el
            break
    return render_template("fish.html", item=item)

from flask import Flask, jsonify, json
@app.route("/api/fishes")
def api_fishes():
    return jsonify([item.toJson() for item in collection])