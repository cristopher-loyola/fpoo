from tkinter import *
from tkinter import ttk
import tkinter as tk
from contolador import Controlador  # Corregido el nombre de la clase


objControlador = Controlador()  # Corregido el nombre de la clase

def ejecutarInsert():
    objControlador.insertUsuario(var1.get(), var2.get(), var3.get())

Ventana = Tk()
Ventana.title("CRUD de usuarios")
Ventana.geometry("500x300")

panel = ttk.Notebook(Ventana)
panel.pack(fill='both', expand='yes')

pestana1 = ttk.Frame(panel)
panel.add(pestana1, text="Crear usuario")

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
Ventana.mainloop()
