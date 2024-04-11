from tkinter import Tk, Frame, Button, Label, messagebox, Entry
import tkinter as tk

Ventana = Tk()
Ventana.title("password")
Ventana.geometry("600x400")

seccion1 = Frame(Ventana)
seccion1.pack(expand=True, fill='both')

Label(seccion1, text="Login FP00", bg="black", fg="white", font=("Mono", 18)).pack()

var1 = tk.StringVar()
Label(seccion1, text="Usuario:", font=("Helvetica", 14)).pack()
Entry(seccion1, takefocus=True, textvariable=var1).pack()

var2 = tk.StringVar()
Label(seccion1, text="Contraseña:", font=("Helvetica", 14)).pack()
Entry(seccion1, show="*", textvariable=var2).pack()

botonAcceso = Button(seccion1, text="Acceder")
botonAcceso.pack()

Ventana.mainloop()
