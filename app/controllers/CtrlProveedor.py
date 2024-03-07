from app.models.proveedor import proveedor
from app.controllers.CtrlMain import CtrlMain
from app.database.mysqlConn import mysqlConn

class CtrlProveedor(CtrlMain):
    def __init__(self,proveedor:proveedor=None):
        if(proveedor!=None):
            self.proveedor=proveedor
        self.connect = mysqlConn(self.conn)
    
    def generateId(self):
        snowflake=self.snowflake()
        self.proveedor.setId(snowflake) 

    def insert(self):
        self.connect.start()
        self.generateId()
        val = (self.proveedor.id, self.proveedor.name,self.proveedor.RFC,self.proveedor.legalName,self.proveedor.legalAddress,self.proveedor.active)
        insertion = self.connect.insert("proveedores",val)
        return {"insertion":insertion,"data":vars(self.proveedor)}

    def update(self,id):
        self.connect.start()
        update = self.connect.update("proveedores",id,vars(self.proveedor))
        return {"update":update,"data":vars(self.proveedor)}

    def delete(self,id):
        self.connect.start()
        delete = self.connect.delete("proveedores",id)
        return {"delete":delete,"data":id}
    
    def get(self,id):
        self.connect.start()
        get = self.connect.get("proveedores",id)
        if(len(get["msg"])==0):
            get["get"]={"code":204,"msg":"No content"}
            return get
        self.proveedor = proveedor(get["msg"][0][1], get["msg"][0][2],get["msg"][0][3],get["msg"][0][4],get["msg"][0][5])
        self.proveedor.setId(get["msg"][0][0])
        return {"get":get,"data":vars(self.proveedor)}
    
    def getAll(self):
        self.connect.start()
        get = self.connect.getAll("proveedores")
        if(len(get["msg"])==0):
            get["get"]={"code":204,"msg":"No content"}
            return get
        self.proveedores=[]
        for p in get["msg"]:
            self.proveedor = proveedor(p[1],p[2],p[3],p[4],p[5])
            self.proveedor.setId(p[0])
            self.proveedores.append(vars(self.proveedor))
        return {"get":get,"data":self.proveedores}

