from flask import Flask
app = Flask(__name__)
import datetime
from flask import render_template
import comp
import comp as Comp

collection = []
def init():
    comp1 = comp.Comp("Laptop")
    collection.append(comp1)
    comp2 = comp.Comp("PC")
    collection.append(comp2)
    comp3 = comp.Comp("Compukter")
    collection.append(comp3)

from flask import request 

@app.route("/comps/new", methods=["GET", "POST"])
def comps_add():
    name = request.form.get("name", default="", type=str)
    age = request.form.get("hdd", default="0", type=float)
    if name:
        comp1 = comp.Comp(name)
        comp1.hdd = hdd
        collection.append(comp1)
    return render_template("new.html")

@app.route('/comps/<name>')
def comp(name):
    item = None
    for el in collection:
        if name == el.name:
            item = el
            break

    return render_template("comp.html", item=item)

@app.route('/comps')
def comps():
    return render_template ("comps.html", collection = collection)

