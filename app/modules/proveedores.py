from flask import Blueprint,request
import json
from app.controllers.CtrlProveedor import CtrlProveedor
from app.models.proveedor import proveedor

#Create a blueprint
proveedores = Blueprint('proveedores', __name__,template_folder='modules')

#CREAR PROVEEDORES
@proveedores.post("/v1/proveedor")
def insertProveedor():
    r = request.json
    p = proveedor(r["name"],r["RFC"],r["legalName"],r["legalAddress"],r["active"])
    ctrl= CtrlProveedor(p)
    insert = ctrl.insert()
    if (insert["insertion"]["code"]==500):
        return json.dumps(insert["insertion"]),409
    return json.dumps(insert["data"]),201

#SHOW ALL
@proveedores.route("/v1/proveedor")
def getAll():
    ctrl= CtrlProveedor()
    authKey = request.args.get("authKey")
    if not(ctrl.kerberos(authKey)):
        return {"msg":"unauthorized"},409
    get = ctrl.getAll()
    if(get["get"]["code"]!=200):
        return json.dumps(get["get"]),get["get"]["code"]
    return json.dumps((get["data"])),200

#BORRAR , BUSCARID Y EDITAR PROVEEDORES
@proveedores.route("/v1/proveedor/<id>",methods=['DELETE','GET','PUT'])
def proveedorRoutes(id):
    # PARA TODOS LOS METODOS PRIMERO SE VA A VALIDAR SI EXITE EL REGISTRO CON EL ID
    ctrl= CtrlProveedor()
    get = ctrl.get(id)
    if(get["get"]["code"]!=200):
        return json.dumps(get["get"]),get["get"]["code"]
    #GET
    if request.method == 'GET':
        return json.dumps(get["data"]),202
    #DELETE
    if request.method == 'DELETE':
        delete =ctrl.delete(id)
        if (delete["delete"]["code"]==500):
            return json.dumps(delete["delete"]),409
        return json.dumps(get["data"]),202
    #PUT(UPDATE)
    if request.method == 'PUT':
        r = request.json
        if ("name" in r):
            ctrl.proveedor.name= r["name"]
        if ("RFC" in r):
            ctrl.proveedor.RFC= r["RFC"]
        if ("legalName" in r):
            ctrl.proveedor.legalName= r["legalName"]
        if ("legalAddress" in r):
            ctrl.proveedor.legalAddress= r["legalAddress"]
        if ("active" in r):
            ctrl.proveedor.active= r["active"]
        update = ctrl.update(id)
        if (update["update"]["code"]==500):
            return json.dumps(update["update"]),409
        return json.dumps(update["data"]),202    