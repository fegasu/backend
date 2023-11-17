from flask import Flask,jsonify,request
import json
import mysql.connector
import pandas as pd

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="APIDB",
    port=3306
)
cursor=conn.cursor()

app=Flask(__name__)
#app.run(debug=True)
@app.route("/",methods=['GET'])
def index():
	return jsonify({"mensaje":"Mi primera API"})

@app.route("/usua",methods=['GET'])
def get_usuarios():
	sql="select * from usuario order by 1"
	listar=EjecutarQuery(sql)
	return listar

@app.route("/usua/s/<id>",methods=['GET'])
def get_usuarios1(id):
	sql="select * from usuario where idusuario="+str(id)+" order by 1"
	listar=EjecutarQuery(sql)
	return listar

@app.route("/usua/i",methods=['POST'])
def post_iusuario():
    json=request.get_json(force=True)
    sql="insert into usuario(login,nombre,apellido,email) values(%s,%s,%s,%s)"
    sqlv=(json["login"],json["nombre"],json["apellido"],json["email"])
    cursor.execute(sql,sqlv)
    conn.commit()
    return "200"

@app.route("/usua/d/<id>",methods=['DELETE'])
def post_dusuario(id):
    sql="delete from usuario where idusuario="+str(id)
    cursor.execute(sql)
    conn.commit()
    return "200"

@app.route("/usua/u/<id>",methods=['PUT'])
def post_ausuario(id):
    json=request.get_json(force=True)
    sql="update usuario set login=%s,nombre=%s,apellido=%s,email=%s where idusuario="+str(id)
    sqlv=(json["login"],json["nombre"],json["apellido"],json["email"])
    cursor.execute(sql,sqlv)
    conn.commit()
    return "200"


def EjecutarQuery(sql):
    cursor.execute(sql)
    row=cursor.fetchall()
    return json.dumps(row)

def Ejecutar(sql):
    cursor.execute(sql)
    conn.commit()
    
    return json.dumps("200")

if __name__ =="__main__":
    app.run(debug=True)
