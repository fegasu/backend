from tkinter import *
import tkinter as tk
from tkinter import messagebox,ttk
import urllib.request
import numpy as np
import json
import sqlite3

modo=False
boton2=None
entry1=None
entry2=None
entry3=None
tabla=None
listar_usuarios=None

class conexion:
    def __init__(self,bd):
        self.basededatos=bd
        self.cnx=sqlite3.connect(self.basededatos)
        self.cursor=self.cnx.cursor()
    
    def ejecutar(sql):
          self.cnx.cursor.execute(sql)
          self.cnx.commit()

    def cerrar():
        self.cnx.close()


def barra_menuppal(root):
    menubar=Menu(root)
    root.config(menu=menubar)
    menuproyecto = Menu(menubar, tearoff=0)
    menusuario = Menu(menubar, tearoff=0)
    menuroles = Menu(menubar, tearoff=0)
    menupruebas = Menu(menubar, tearoff=0)
    menuejecucion = Menu(menubar, tearoff=0)
    menuayuda = Menu(menubar, tearoff=0)

    menubar.add_cascade(label="Proyectos", menu=menuproyecto)
    menubar.add_cascade(label="Usuarios", menu=menusuario)
    menubar.add_cascade(label="Roles", menu=menuroles)
    menubar.add_cascade(label="Pruebas", menu=menupruebas)
    menubar.add_cascade(label="Ejecución de Pruebas", menu=menuejecucion)
    menubar.add_cascade(label="Ayuda", menu=menuayuda)
    menusuario.add_command(label="Administra",command=Usuario)
    menusuario.add_command(label="Usuarios/Roles")


    menuproyecto.add_separator()
    menuproyecto.add_command(label="Salir", command=lambda:Salir(root))

def Ejecutado(url):
    url=url.replace(chr(32),'+')
    try:
        miurl=urllib.request.urlopen(url)
    except ValueError:
        messagebox.showerror("Rutinas/Ejecutado","Ocurrio un error")
    return miurl

def EtiquetaForma(ventana,titulo,fila,columna):
    etiqueta1=tk.Label(ventana,text=titulo)
    etiqueta1.grid(row=fila,column=columna)
    return etiqueta1

def Entrada(ventana,ancho=0,fila=0,col=0,une=0,entrada=None,accion=None):
    entrada=tk.Entry(ventana,textvariable=entrada)
    entrada.grid(row=fila,column=col,ipadx=ancho)
    if une>0:
        entrada.grid(columnspan=une)
    if ancho>0:
        entrada.grid(row=fila,column=col,ipadx=ancho)
    return entrada

def Boton(ventana,titulo,ancho,fila,col,accion=""):
    boton1=tk.Button(ventana,text=titulo)
    boton1.grid(row=fila,column=col,ipadx=ancho)
    boton1.config(font=('Arial',12,'bold'),width=15,
        bg='#036C1B',fg='#FAF550',activebackground="#35BD6F",relief='flat',command=accion)
    return boton1

def CargaDatos(url):
    try:
        url=url.replace(chr(32),'+')
        #print("->"+url)
        miurl=urllib.request.urlopen(url)

        miarreglo=json.loads(miurl.read().strip())
        return miarreglo
    except:
        messagebox.showerror("Conectando","Ocurrio un error")

def Editar_datos():
    global tabla,boton2,entry1,entry2,entry3
    pass

def limpiarcampos():
    global entry1,entry2,entry3
    pass

def recargar():
    global tabla
    pass

def getIdUsuario():
    global tabla
    pass

def NuevoUsuario():
    global tabla
    pass
    
def Borrar_datos():
    global tabla
    pass

def Actualizar_datos():
    global tabla
    pass

def Grilla(ventana,fila,col,columnas,titulos,datos,une=1):
    global tabla
    tabla=ttk.Treeview(ventana,columns=(columnas))
    i=0
    for row in titulos:
        tabla.heading("#"+str(i),text=row)
        i=i+1
    tabla.grid(row=fila,column=col,columnspan=une)
    CargaGrilla()
    return tabla

def CargaGrilla():
    global tabla, listar_usuarios
    registros=tabla.get_children()
    #borra filas de la grilla
    for registro in registros:
        tabla.delete(registro)
    #inserta valores en la grilla
    #for p in listar_usuarios:
    #        tabla.insert('',0,text=p[0],values=(p[2],p[3],p[4]))
    

def Salir(ventana):
    if messagebox.askyesno(message="Desea Terminar?",title="Terminar"):
        ventana.destroy()

def CargaCombo(url,ventana):
    combo=ttk.Combobox(ventana,state="readonly")
    combo['values'] = CargaDatos(url)
    return combo

def deshabilitaCajas(estado):
    global modo,entry1,entry2,entry3
    pass

def cancelarTodo():
    global modo,entry1,entry2,entry3,boton2
    deshabilitarBoton('disabled',boton2)

def deshabilitarBoton(estado,boton):
    boton["state"]=estado    

def  EjecutarQuery(bd,sql):
    cnx1=sqlite3.connect(bd)
    cursor=cnx1.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    return json.dumps(rows)

    
def Usuario():
    global listar_usuarios,tabla,boton2,entry1,entry2,entry3
    print("Iniciando modulo usuarios")
    ven1=tk.Toplevel()
    ven1.geometry("900x400")
    style = ttk.Style()
    style.theme_use('clam')
    ven1.config(padx=10,pady=10,relief="sunken",bd=6)
    ven1.iconbitmap("img/logosenacir.ico")
    ven1.title('TESTSENA - MANEJO DE USUARIOS')
    ven1.resizable(0,0)
    tabla=Grilla(ven1,5,0,('NOMBRE','APELLIDO','EMAIL'),
            ('ID','NOMBRE','APELLIDO','EMAIL'),listar_usuarios,4)
    etiqueta1=EtiquetaForma(ven1,"Nombre:",0,0)
    entry1=Entrada(ven1,110,0,1,2)
    etiqueta2=EtiquetaForma(ven1,"Apellidos:",1,0)
    entry2=Entrada(ven1,110,1,1,2)
    etiqueta3=EtiquetaForma(ven1,"Email:",2,0)
    entry3=Entrada(ven1,110,2,1,2)
    boton1=Boton(ven1,"NUEVO",10,3,0,lambda:NuevoUsuario())
    boton2=Boton(ven1,"GRABAR",10,3,1,lambda:Actualizar_datos())
    boton3=Boton(ven1,"CANCELAR",10,3,2,lambda:desabilitaCajas('disabled')   
    )    
    botonEditar=Boton(ven1,"EDITAR",20,6,0,lambda:Editar_datos())
    botonEliminar=Boton(ven1,"ELIMINAR",20,6,1,lambda: Borrar_datos())
    botonTerminar=Boton(ven1,"TERMINAR",20,6,2,lambda:Salir(ven1))
    desabilitaCajas('disabled')	
    deshabilitarBoton('disabled',boton2)
    ven1.protocol("WM_DELETE_WINDOW", lambda:Salir(ven1))

         	
def main():
    ventana= Tk()
    ventana.title('TESTSENA - SISTEMA DE PRUEBAS DE SOFTWARE V1.0 2021')
    ventana.resizable(0,0)
    ventana.geometry("550x620")
    ventana.iconbitmap("img/logosenacir.ico")
    ventana.config(padx=5,pady=10,relief="sunken",bd=5)
    logo=tk.PhotoImage(file='img/ADSI1.png')
    logo1=tk.Label(ventana,image=logo).pack()
    barra_menuppal(ventana)
    tabla=ttk.Treeview(ventana,column=4)
    ventana.protocol("WM_DELETE_WINDOW", lambda:Salir(ventana))
    ventana.mainloop()

if __name__ =="__main__":
    print("Iniciando Aplicacion")
    main()

