import os
import json
import modules.utils as ut
import modules.messages as msg

MY_DATABASE = None

def NewFile(*param):
    with open(MY_DATABASE,"w") as wf:
        json.dump(param[0],wf,indent=4)

def ReadFile():
    with open(MY_DATABASE,"r") as rf:
        return json.load(rf)
    
def AddData(*param):
    with open(MY_DATABASE,"r+") as rwf:
        data_file=json.load(rwf)
        if (len(param) > 1):
            try:
                data_file.get(param[0]).update(param[1])
            except AttributeError:
                pass
                # data_file.get(param[0]).update({param[1]:param[2]})
            # data_file.update({param[0]:param[1]})
        else:
            data_file.update({param[0]})
        # data_file[llavePrincipal].update({codigo:info})
        rwf.seek(0)
        json.dump(data_file,rwf,indent=4)

def checkFile(*param):
    data = list(param)
    if(os.path.isfile(MY_DATABASE)):
        if(len(param)):
            data[0].update(ReadFile())
    else:
        if(len(param)):
            NewFile(data[0])