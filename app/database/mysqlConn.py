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

    