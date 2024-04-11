from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
from controlador import controlador
from GeneradorPDF import*
objControlador = controlador()
objPDF = GeneradorPDF ()

def ejecutarInsert():
    objControlador.insertUsuario(var1.get(), var2.get(), var3.get())
    
def buscarUsuario():
    usuarioBD = objControlador.buscarUsuario(varBus.get())
    if not usuarioBD:
        messagebox.showwarning("Nada", "Id no existe en BD")
    else:
        text_result.delete(1.0, END)
        text_result.insert(END, usuarioBD)
def mostrarUsuarios():
    usuarios = objControlador.mostrarTodosUsuarios()
    texto_usuarios = ''
    for usuario in usuarios:
        texto_usuarios += f"ID: {usuario[0]}, Nombre{usuario[1]}, correo:{usuario[2]}, Contrasena:{usuario[3]}\n"
    
    
    textRegistro.insert("end", texto_usuarios)
    
def ejecutarPDf():
        if varTitulo =="":
            messagebox.showwarning("Importante, escribe un nombre")
        else:
            objPDF.add_page()
            objPDF.chapter_body()
            objPDF.output(varTitulo.get()+".pdf")
            rutaPDF ="C/Users/USUARIO/Documents/github/fpoo/tkSQLite/GeneradorPDF.py"+varTitulo.get()+".pdf"
            messagebox.showinfo("Archivo creado", "Pdf disponible")
            os.system(f"start {rutaPDF}")
        
Ventana = Tk()
Ventana.title("CRUD de usuarios")
Ventana.geometry("500x300")

panel = ttk.Notebook(Ventana)
panel.pack(fill='both', expand='yes')

pestana1= ttk.Frame(panel)
pestana2= ttk.Frame(panel)
pestana3= ttk.Frame(panel)
pestana4= ttk.Frame(panel)
pestana5= ttk.Frame(panel)
pestana6= ttk.Frame(panel)

panel.add(pestana1,text="Crear usuario")
panel.add(pestana2,text="Buscar usuario")
panel.add(pestana3,text="Consultar usuario")
panel.add(pestana4,text="Editar usuario")
panel.add(pestana5,text="Eliminar usuario")
panel.add(pestana6,text="Exportar en PDF")

Label(pestana1, text="Registro de usuarios", fg="blue", font=("Modern", 18)).pack()

var1 = tk.StringVar()
Label(pestana1, text="Nombre: ").pack()
Entry(pestana1, textvariable=var1).pack()

var2 = tk.StringVar()
Label(pestana1, text="Correo: ").pack()
Entry(pestana1, textvariable=var2).pack()

var3 = tk.StringVar()
Label(pestana1, text="Contraseña: ").pack()
Entry(pestana1, textvariable=var3).pack()

Button(pestana1, text="Guardar usuario", command=ejecutarInsert).pack()

Label(pestana2, text="Buscar usuario", fg="red", font=("Mono", 18)).pack()
varBus = tk.StringVar()
Label(pestana2, text="id: ").pack()
Entry(pestana2, textvariable=varBus).pack()

Button(pestana2, text="buscarUsuario", command=buscarUsuario).pack()

Label(pestana2, text="Registrado: ", fg="blue", font=("Mono", 16)).pack()
text_result = Text(pestana2, height=5, width=52)
text_result.pack()

Label(pestana3, text="Consultar usuarios", fg="blue", font=("Mono", 18)).pack()
Button(pestana3, text="consultar", command=mostrarUsuarios).pack()
textRegistro = tk.Text(pestana3, height=30, width=60)
textRegistro.pack()

#pestaña 6:Exportar pdf
Label(pestana6, text="Usuarios en PDF", fg="blue", font=("Mono", 18)).pack()
varTitulo= tk.StringVar()
Label(pestana6, text="Escribe el codigo de tu usuario", fg="black", font=("Mono", 10)).pack()
Entry(pestana6, textvariable=var1).pack()
Button(pestana6, text="Crear PDF", command=ejecutarPDf).pack()
textRegistro.pack()
Ventana.mainloop()