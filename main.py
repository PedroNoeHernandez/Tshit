from flask import Flask
from flask import Blueprint
from flask import request
import json
from app.modules.proveedores import proveedores

app = Flask(__name__)
app.register_blueprint(proveedores)
config = json.load( open('./config.json'))


@app.route("/")

def index():
    return '{message:"helloworld"}'

@app.route("/v1/inventario")

def get():
    return '{message:"helloworld"}'

@app.route("/v1/inventario/productos")
def productos():
    return '''[{"id":1,"name":"Mustard Prepared","price":95,"category":"Major Pharmaceuticals","stock":false,"size":"3XL"},
            {"id":2,"name":"Milk - 2% 250 Ml","price":19,"category":"Oilfield Services/Equipment","stock":true,"size":"XS"},
            {"id":3,"name":"Wine - White Cab Sauv.on","price":13,"category":"Computer Software: Prepackaged Software","stock":false,"size":"L"},
            {"id":4,"name":"Phyllo Dough","price":9,"category":"Property-Casualty Insurers","stock":false,"size":"XL"},
            {"id":5,"name":"Vodka - Hot, Lnferno","price":51,"category":"Major Banks","stock":false,"size":"XS"},
            {"id":6,"name":"Garam Masala Powder","price":26,"category":"n/a","stock":true,"size":"2XL"},
            {"id":7,"name":"Avocado","price":59,"category":"Professional Services","stock":true,"size":"L"},
            {"id":8,"name":"Bagel - 12 Grain Preslice","price":19,"category":"Electric Utilities: Central","stock":true,"size":"3XL"},
            {"id":9,"name":"Pear - Asian","price":1,"category":"n/a","stock":true,"size":"S"},
            {"id":10,"name":"Onions Granulated","price":99,"category":"Military/Government/Technical","stock":false,"size":"XL"}]'''



    