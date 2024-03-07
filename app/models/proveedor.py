class proveedor:

    def __init__(self,name:str,RFC:str,legalName:str,legalAddress:str,active:int):
        self.name = name
        self.RFC = RFC
        self.legalName = legalName
        self.legalAddress = legalAddress
        self.active = active

    def setId(self,id:str):
        self.id= id