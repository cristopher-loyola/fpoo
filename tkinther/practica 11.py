from tkinter import Tk,Frame

#Creamos la ventana 
Ventana= Tk() #Uso de POO creando un objeto ventana
Ventana.title("Ejemplo con 3 frames")
Ventana.geometry("600x400")

seccion1=Frame(Ventana,bg="red")
seccion1.pack()

seccion2=Frame(Ventana,bg= "yellow")
seccion2.pack()

seccion3=Frame(Ventana)
seccion3.pack()

#Ejecuta la ventana 
Ventana.mainloop()