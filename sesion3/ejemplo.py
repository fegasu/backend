import urllib.request
import numpy as np
import json
import requests
from requests import Session
PostG=None


def EjecutaRest(url,metodo,datos):
    global PostG
    url=url.replace(chr(32),'+')
    miurl=None
    try:
        if metodo=="POST":
            miurl=requests.post(url,json=datos)
        if metodo=="PUT":
            miurl=requests.put(url,json=datos)
        if metodo=="DELETE":
            miurl=requests.delete(url)
        if metodo=="GET":
            miurl=requests.get(url)
            miurl=EjecutaGet(url)
            #    miurl1=urllib.request.urlopen(url)
            #    miurl=json.loads(miurl1.read().strip())
        return miurl
    except ValueError:
        messagebox.showerror("Rutinas/EjecutaRest","Ocurrio un error")

def EjecutaGet(url):
    #miurl1=urllib.request.urlopen(url)
    #miurl=json.loads(miurl1.read().strip())
    miurl1= urllib.request.urlopen(url)
    miurl = miurl1.read().decode("utf8")
    #print("->"+miurl)
    return miurl


datos={
    "IdUsuario":3,
	"nombre":"Maria",
	"apellido":"La bandida",
	"email":"emadera@gmail.com"
}



#print(EjecutaRest('http://127.0.0.1:5000/usua/i','POST',datos))
#print(EjecutaRest('http://127.0.0.1:5000/usua/s/0','GET',None))
#print(EjecutaRest('http://127.0.0.1:5000/usua/u/3','PUT',datos))
#print(EjecutaRest('http://127.0.0.1:5000/usua/d/3','DELETE',datos))
print(EjecutaRest('http://127.0.0.1:5000/usua/s/0','GET',None))

