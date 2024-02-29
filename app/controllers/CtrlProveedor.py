from app.models.proveedor import proveedor
from app.controllers.CtrlMain import CtrlMain
from app.database.mysqlConn import mysqlConn

class CtrlProveedor(CtrlMain):
    def __init__(self,proveedor:proveedor):
        self.proveedor=proveedor
        self.connect = mysqlConn(self.conn)
    
    def generateId(self):
        snowflake=self.snowflake()
        proveedor.setId(proveedor,snowflake) 

    def insert(self):
        self.connect.start()
        sql = "INSERT INTO proveedores (id, name, RFC, legalName, legalAddress, active) VALUES (%s, %s, %s,%s,%s,%s)"
        val = (self.proveedor.id, self.proveedor.name,self.proveedor.RFC,self.proveedor.legalName,self.proveedor.legalAddress,self.proveedor.active)
        self.connect.cursor.execute(sql, val)
        self.connect.connect.commit()
        self.connect.cursor.close()
        return self.proveedor

    # def update():
    # def delete():