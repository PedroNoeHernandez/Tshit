# TShit

## clone the repository

```cmd
git clone "{url}"
```
visualiza la estructura de archivos en del repositorio

## Corregir la conexión a la base de datos

### Paso1
1. Agrega al archivo de configuración el atributo database.schema en el archivo config.json y coloca las credenciales d etu base de datos
```
...
"database":{
        "host":"localhost",
        "user":"root",
        "password":"root",
        "schema":"tshirt"
    },
...
```

2. Importa las bibliotecas os.path, json y manda a llamar la configuración el archivo config.json en lugar de las cadenas en el código

```python
import mysql.connector
import os.path
import json

class mysqlConn:
    
    def __init__(self,config):
        config = json.load( open('./config.json'))
        database = config['database']
        self.connect =mysql.connector.connect(
        host=database["host"],
        user=database["user"],
        password=database["password"],
        database=database["schema"]
        )
#### ...
```
 3. Prueba el correcto funcionamiento de la app 

```flask --app main run --debug```

## Generar un token nuevo en lugar de usar el id de usuario

1. Borra la siguiente validación en module/auth
``` python
@auth.post("/v1/auth")
def login():
#...
for key in authKeys:
            if not key in r:
                return '{"msg":"missing' +f'{key}"'+'}',401
#...
```
2. borra la validación de existencia el archivo que tiene el nombre del id en la función get gredentials

3. utiliza la función snowflake para generar una nueva llave como nombre de archivo y valor de retorno como data en lugar del Id del usuario en app/controllers/CtrlUser.py

```python
def getCredentials(self,email,passwd):
#...
#escribir credenciales en servidor
        key = self.snowflake()
        with open(path+"/"+f"{key}.json", 'w') as file:
            json.dump(vars(self.user), file)
        #regresar llave
        return {"code":200,"get":get,"data":key}
#...
```
4. Prueba en post man loguearte varias veces y explica por qué el resultado en los casos no es el mismo

5. Analiza qué ventajas tiene que se genere más de una llave por usuario y qué desventajas podría tener (revisa la carpoeta auth)

