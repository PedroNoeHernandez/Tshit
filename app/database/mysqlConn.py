import mysql.connector

class mysqlConn:
    
    def __init__(self,config):
        self.connect =mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="tshit"
        )
    def start(self):
        self.cursor = self.connect.cursor()
    def stop(self):
        self.cursor.close()
        self.connect.close()
    
### INSERT

    def insert(self,table:str,values:list):
        sql = f"INSERT INTO {table} VALUES ("
        for i in range(0,len(values)-1):
            sql = sql + " %s,"
        sql= sql+ "%s)"
        try:
            self.cursor.execute(sql, values)
            self.connect.commit()
            self.cursor.close()
            return {"code":200,"msg":"Successfully inserted"}
        except (mysql.connector.Error) as e:
            return {"code":500,"msg":e.msg}
    
### UPDATE
    def update(self,table:str,id:str,values:dict):
        sql = f"UPDATE {table} SET "
        sqlSets = []
        for key in values:
            if(type(values[key])is int):
                sqlSets.append( f"{key} = {values[key]}")
            else:
                sqlSets.append( f"{key} = '{values[key]}'")
        sql =sql + ", ".join(sqlSets)
        sql = sql+ f" WHERE id = '{id}'"
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            self.cursor.close()
            return {"code":200,"msg":"Updated Successfully"}
        except (mysql.connector.Error) as e:
            return {"code":309,"msg":e.msg}


### DELETE
    def delete(self,tabla:str, id:str):
        sql = f"DELETE FROM {tabla} WHERE id ='{id}'"
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            self.cursor.close()
            return {"code":200,"msg":"Successfully deleted"}
        except (mysql.connector.Error) as e:
            return {"code":309,"msg":e.msg}


### GET ALL
    def getAll(self,tabla:str):
        sql = f"SELECT * FROM {tabla}"
        try:
            self.cursor.execute(sql)
            myresult = self.cursor.fetchall()
            self.cursor.close()
            return {"code":200,"msg":myresult}
        except (mysql.connector.Error) as e:
            return {"code":309,"msg":e.msg}

### GET
    def get(self,tabla:str, id:str):
        sql = f"SELECT * FROM {tabla} WHERE id ='{id}'"
        try:
            self.cursor.execute(sql)
            myresult = self.cursor.fetchall()
            self.cursor.close()
            return {"code":200,"msg":myresult}
        except (mysql.connector.Error) as e:
            return {"code":309,"msg":e.msg}

### SEARCH

    