from flask import Blueprint,request
import json
from app.controllers.CtrlProveedor import CtrlProveedor
from app.models.proveedor import proveedor

#Create a blueprint
proveedores = Blueprint('proveedores', __name__,template_folder='modules')


@proveedores.post("/v1/proveedor")
def insertProveedor():
    p = proveedor(request.json)
    ctrl= CtrlProveedor(p)
    ctrl.generateId()
    ctrl.insert()
    return json.dumps(ctrl.proveedor.__dict__) 