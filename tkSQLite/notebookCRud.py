from tkinter import *
from tkinter import ttk
import tkinter as tk

Ventana= Tk()
Ventana.title("CRUD de Usuarios")
Ventana.geometry("500x300")

panel= ttk.Notebook(Ventana)
panel.pack(fill='both', expand="yes")

pestana1= ttk.Frame(panel)
pestana2= ttk.Frame(panel)
pestana3= ttk.Frame(panel)
pestana4= ttk.Frame(panel)
pestana5= ttk.Frame(panel)



panel.add(pestana1, text="Crear Usuario")
panel.add(pestana2, text="Buscar Usuario")
panel.add(pestana3, text="Consultar Usuarios")
panel.add(pestana4, text="Edita Usuario")
panel.add(pestana5, text="Eliminar Usuario")

#pestaña 1:formulario de insert
Label(pestana1, text="Registro de usuarios", fg="blue", font=("Modern",18)).pack()

var1= tk.StringVar()
Label(pestana1,text="nombre").pack()
Entry(pestana1, textvariable=var1).pack()

var2= tk.StringVar()
Label(pestana1,text="correo: ").pack()
Entry(pestana1, textvariable=var1).pack()

var3= tk.StringVar()
Label(pestana1,text="contraseña: ").pack()
Entry(pestana1, textvariable=var1).pack()

Button(pestana1,text="Guardae usuario").pack()




Ventana.mainloop()
