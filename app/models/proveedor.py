class proveedor:

    def __init__(self,json):
        self.name = json["name"]  
        self.RFC = json["RFC"]  
        self.legalName = json["legalName"]
        self.legalAddress = json["legalAddress"]  
        self.active = json["active"]
    def setId(self,id:str):
        self.id= id