import os
import json

MY_DATABASE = None # Base de datos vacia

def NewFile(*param): # Crear archivo json
    with open(MY_DATABASE,"w") as wf:
        json.dump(param[0],wf,indent=4)

def ReadFile(): # leer archivo json
    with open(MY_DATABASE,"r") as rf:
        return json.load(rf)

def checkFile(*param): # Verificar archivo json
    data = list(param)
    if(os.path.isfile(MY_DATABASE)): # Si ya existe lo lee
        if(len(param)):
            data[0].update(ReadFile())
    else: # Si no existe lo crea
        if(len(param)):
            NewFile(data[0])

def AddData(origin): # Guardar informacion en el archivo json
    with open(MY_DATABASE,"w") as rwf:
        json.dump(origin,rwf,indent=4)