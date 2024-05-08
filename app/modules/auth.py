from flask import Blueprint,request
import json
from app.controllers.CtrlUser import CtrlUser
from app.models.user import user

#Create a blueprint
auth = Blueprint('auth', __name__,template_folder='modules')
keys = ["name","user","email","status","type","passwd","passwd2"]
#CREAR users
@auth.post("/v1/signUp")
def signUp():
    r = request.json
    #validate if contain all data
    for key in keys:
        if not key in r:
            return '{"msg":"missing' +f'"{key}"'+'}',409
    
    if (r["passwd"]!=r["passwd2"]):
        return '{"msg":"password not match"}',409

    u = user(r["name"],r["user"],r["email"],r["status"],r["type"],r["passwd"])
    ctrl= CtrlUser(u)
    insert = ctrl.insert()
    if (insert["insertion"]["code"]==500):
        return json.dumps(insert),409
    return json.dumps(insert["data"]),201


#BORRAR , BUSCARID Y EDITAR users
@auth.route("/v1/user/<id>",methods=['DELETE','GET','PUT'])
def proveedorRoutes(id):
    # PARA TODOS LOS METODOS PRIMERO SE VA A VALIDAR SI EXITE EL REGISTRO CON EL ID
    ctrl= CtrlUser()
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
        for key in keys:
            if (key in r):
                ctrl.user[key]= r[key]
        update = ctrl.update(id)
        if (update["update"]["code"]==500):
            return json.dumps(update["update"]),409
        return json.dumps(update["data"]),202

#Auth
@auth.post("/v1/auth")
def login():
    r = request.json
    authKeys=["email","passwd"]
    for key in authKeys:
            if not key in r:
                return '{"msg":"missing' +f'{key}"'+'}',401
    #hacer authenticación
    ctrl= CtrlUser()
    auth = ctrl.getCredentials(r["email"],r['passwd'])
    if (auth["code"]==200):
        return auth["data"],200
    return auth["msg"] ,auth["code"]

