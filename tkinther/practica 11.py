from tkinter import Tk,Frame, Button,messagebox
#metodos para mensaje
def mostrarMensajes():
    print(messagebox.showinfo('showinfo', 'information'))
    print(messagebox.showerror('showinfo', 'information'))
    print(messagebox.showwarning('showinfo', 'information'))
    print(messagebox.askokcancel(message="¿Desea continuar?", title="Soy el titulo"))
    

def addbtn():
    botonVerde.config(text="+")
    botonRosa=Button(seccion3,text="nuevo", bg="pink")
    botonRosa.configure(height=2,width=10)
    botonRosa.pack()
    
#Creamos la ventana 
Ventana= Tk() #Uso de POO creando un objeto ventana
Ventana.title("Ejemplo con 3 frames")
Ventana.geometry("600x400")

seccion1=Frame(Ventana,bg="red")
seccion1.pack(expand= True,fill='both')

seccion2=Frame(Ventana,bg= "yellow")
seccion2.pack(expand= True,fill='both')

seccion3=Frame(Ventana)
seccion3.pack(expand= True,fill='both')

#botones

botonAzul= Button(seccion1,text="Azul",fg="blue")
botonAzul.place(x=60,y=60, width=100, height=30)

#grid
botonNegro= Button(seccion2,text="Negro", fg="Black",bg="black")
botonNegro.configure(heigh=2,width=10)
botonNegro.grid(row=0,column=1)

botonAmarillo=Button(seccion2,text="Amarillo", bg="yellow",command=mostrarMensajes)
botonAmarillo.configure(height=2,width=10)
botonAmarillo.grid(row=1, column=2)

botonVerde=Button(seccion3,text="Verde", bg="green",command=addbtn)
botonVerde.configure(height=2,width=10)
botonVerde.pack()


#Ejecuta la ventana 
Ventana.mainloop()

