from flask import Flask,render_template,request
import numpy as np
import json
from flask import render_template

#https://j2logo.com/flask/tutorial-como-crear-api-rest-python-con-flask/

listar=None
cnx1=None
#tipo="sqlite3"
config={"tipo":"mysql"
        ,"bd":"init.dat"
        } # sqlite3 mysql postgres
print(config["tipo"])
app = Flask(__name__)
def Conexion():
    global config
    try:
        #****************CONECTANDO CON SQLITE ***********
        if config["tipo"]=="sqlite3":
            import sqlite3
            bd=config["bd"]
            cnx=None
            cnx=sqlite3.connect(bd)
        if config["tipo"]=="mysql":
            #****************CONECTANDO CON MYSQL ***********
            import mysql.connector
            cnx=None
            cnx=mysql.connector.connect(user="root",password="root",host="localhost",
                database="registro")
        if config["tipo"]=="postgres":
        #****************CONECTANDO CON POSTGRES ***********
            import psycopg2
            cnx=None
            cnx = psycopg2.connect(database="postgres", user="postgres", password="", 
            host="127.0.0.1", port="5432")
    except ValueError:
        print("Fallo la conexion a la base de datos")
    return cnx


def  EjecutarQuery(bd,sql):
    cnx1=Conexion()
    cursor=cnx1.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    return json.dumps(rows)

def  Ejecutar(bd,sql):
    global tipo
    cnx1=Conexion()
    cursor1=cnx1.cursor()
    cursor1.execute(sql)
    cnx1.commit()
    cursor1.close()
    return json.dumps("200")



@app.route("/usua/s/<id>", methods=['GET'])
def usuario(id=0):
    if id=="0":
        sql='select * from usuario order by 1 asc'
    else:
        sql='select * from usuario where "idUsuario"='+str(id)+' order by 1 asc'
    listar=EjecutarQuery("init.dat",sql)
    return listar

@app.route('/usua/i', methods=['POST'])
def iusuario():
    global listar
    json = request.get_json(force=True)
    sql="insert into usuario(nombre,apellido,email) values('"+json["nombre"]+"','"+json["apellido"]+"','"+json["email"]+"')"    
   
    Ejecutar("init.dat",sql)
    return sql

@app.route('/usua/u/<id>', methods=['PUT'])
def ausuario(id):
    global listar
    json = request.get_json(force=True)
    sql="update usuario set nombre='"+json["nombre"]+"',apellido='"+json["apellido"]+"',email='"+json["email"]+"' where \"idUsuario\"="+str(id)
    Ejecutar("init.dat",sql)
    return ""

@app.route('/usua/d/<id>', methods=['DELETE'])
def dusuario(id):
    try:
        sql="delete from usuario where \"idUsuario\"="+str(id)
        Ejecutar("init.dat",sql)
        return "USUARIO BORRADO"
    except ValueError:
        return "ERROR AL BORRAR EL USUARIO"


@app.route("/estado")
def estado():
    global listar
    listar=EjecutarQuery("init.dat",'select * from estado')
    print(listar)
    return listar

@app.route("/help")
@app.route("/")
def main():
    return render_template("notas.html")
    #return "<p>Mi primera API-REST</p>"

#cnx1.close()