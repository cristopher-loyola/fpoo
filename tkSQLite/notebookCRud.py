from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
from controlador import controlador

objControlador = controlador()

def ejecutarInsert():
    objControlador.insertUsuario(var1.get(), var2.get(), var3.get())
    
def buscarUsuario():
    usuarioBD = objControlador.buscarUsuario(varBus.get())
    if not usuarioBD:
        messagebox.showwarning("Nada", "Id no existe en BD")
    else:
        text_result.delete(1.0, END)
        text_result.insert(END, usuarioBD)

Ventana = Tk()
Ventana.title("CRUD de usuarios")
Ventana.geometry("500x300")

panel = ttk.Notebook(Ventana)
panel.pack(fill='both', expand='yes')

#3 definir las pestañas del nootbook
pestana1= ttk.Frame(panel)
pestana2= ttk.Frame(panel)
pestana3= ttk.Frame(panel)
pestana4= ttk.Frame(panel)
pestana5= ttk.Frame(panel)


#4 agregamos las pestañas
panel.add(pestana1,text="Crear usuario")
panel.add(pestana2,text="Buscar usuario")
panel.add(pestana3,text="Consultar usuario")
panel.add(pestana4,text="Editar usuario")
panel.add(pestana5,text="Eliminar usuario")

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

Ventana.mainloop()
