import tkinter as tk
import random
import string
from funciones import *
from tkinter import Tk, Frame, Button, Label, messagebox, Entry
import tkinter as tk

Ventana = Tk()
Ventana.title("password")
Ventana.geometry("600x400")

seccion1 = Frame(Ventana)
seccion1.pack(expand=True, fill='both')

Label(seccion1, text="matricula", bg="black", fg="white", font=("Mono", 18)).pack()

var1 = tk.StringVar()
Label(seccion1, text="nombre: ", font=("Helvetica", 14)).pack()
Entry(seccion1, takefocus=True, textvariable=var1).pack()

var2 = tk.StringVar()
Label(seccion1, text="Apellido paterno :", font=("Helvetica", 14)).pack()
Entry(seccion1, takefocus=True, textvariable=var1).pack()

var3 = tk.StringVar()
Label(seccion1, text="apellido materno:", font=("Helvetica", 14)).pack()
Entry(seccion1, takefocus=True, textvariable=var1).pack()

var4 = tk.StringVar()
Label(seccion1, text="Año de nacimiento: ", font=("Helvetica", 14)).pack()
Entry(seccion1, takefocus=True, textvariable=var1).pack()

var5 = tk.StringVar()
Label(seccion1, text="Carrera: ", font=("Helvetica", 14)).pack()
Entry(seccion1, takefocus=True, textvariable=var1).pack()

var6 = tk.StringVar()
Label(seccion1, text="año en curso: ", font=("Helvetica", 14)).pack()
Entry(seccion1, takefocus=True, textvariable=var1).pack()



Ventana.mainloop()
