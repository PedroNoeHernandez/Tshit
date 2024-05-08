class user:
    
    def __init__(self,name:str,user:str,email:str,status:int,type:int,passwd:str):
        self.name = name
        self.user = user
        self.email = email
        self.status = status
        self.type = type
        self.passwd = passwd

    def setId(self,id:str):
        self.id= id
        