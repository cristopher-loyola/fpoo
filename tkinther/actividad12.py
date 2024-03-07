import tkinter as tk
from tkinter import Tk,Frame, Button,messagebox,ttk,Entry
from main import persona

#creacion de la ventana
ventana= Tk()
ventana.title ("Login de usuario")
ventana.geometry("600x600")

seccion1= Frame(ventana, bg="white")
seccion1.pack(expand= True,fill='both')

#input 

etiqueta1 = tk.Label(ventana, text="Usuario")
etiqueta1.pack()

entrada1 = tk.Entry(ventana)
entrada1.pack()

etiqueta2 = tk.Label(ventana, text="contraseña")
etiqueta2.pack()

entrada2 = tk.Entry(ventana)
entrada2.pack()


#botones
validar= Button(text="Validar",fg="black")
validar.place(x=230,y=60, width=100, height=30)

#funcion
def verificar_usuario():
    usuario_ingresado = entrada_usuario.get()

    if usuario_ingresado in usuarios_registrados:
        print(messagebox.showinfo('usuario registrado'))
    else:
        print(messagebox.showinfo('usuario no registrado'))



#ejecutar ventana
ventana.mainloop()
