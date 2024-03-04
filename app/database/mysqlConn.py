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
            return "Successfully inserted"
        except (MySQLdb.Error, MySQLdb.Warning) as e:
            return e
        finally:
            self.cursor.close()

### DELETE
    def delete(tabla:str, id:str):
        sql = f"DELETE FROM {tabla} WHERE id ='{id}'"
        try:
            self.cursor.execute(sql)
            self.connect.commit()
        except (MySQLdb.Error, MySQLdb.Warning) as e:
            return e
        finally:
            self.cursor.close()


### GET ALL

### SEARCH

    