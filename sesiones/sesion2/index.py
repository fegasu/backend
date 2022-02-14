from flask import Flask,render_template,request
import sqlite3
import json

app=Flask(__name__)
app.run(debug=True)
@app.route("/")
def xx():
	return "<p>Mi primera ruta del dia de hoy</p>"

@app.route("/usua/s/<id>",methods=['GET'])
def usuario(id=0):
	if id=="0":
		sql="select * from persona order by 1"
	else:
		sql="select * from persona where idPersona="+str(id)+" order by 1"
	listar=EjecutarQuery("SALUD.db",sql)
	return listar

@app.route("/usua/i",methods=['POST'])
def iusuario():
	json=request.get_json(force=True)
	sql="insert into persona(idpersona,tipoidentificacion,nombre,apellido) values("+str(json["idpersona"])+","+str(json["tipoidentificacion"])+",'"+json["nombre"]+"','"+json["apellido"]+"')"
	
	print(sql)
	Ejecutar("SALUD.db",sql)
	return sql

@app.route("/usua/u/<id>",methods=['PUT'])
def ausuario(id):
	json=request.get_json(force=True)
	sql="update persona set idpersona="+str(json["idpersona"])+",tipoidentificacion="+str(json["tipoidentificacion"])+",nombre='"+json["nombre"]+"',apellido='"+json["apellido"]+"' where idpersona="+str(id)
	Ejecutar("SALUD.db",sql)
	return sql
@app.route("/usua/d/<id>",methods=['DELETE'])
def dusuario(id):
	sql="delete from  persona where idpersona="+str(id)
	Ejecutar("SALUD.db",sql)
	return sql

def EjecutarQuery(bd,sql):
	cnx1=sqlite3.connect(bd)
	cursor=cnx1.cursor()
	cursor.execute(sql)
	row=cursor.fetchall()
	return json.dumps(row)

def Ejecutar(bd,sql):
	cnx1=sqlite3.connect(bd)
	cursor=cnx1.cursor()
	cursor.execute(sql)
	cnx1.commit()
	cnx1.close()
	return json.dumps("200")
