from persona import *

#solicitar datos del usuario
id =int(input("Escribe tu id: "))
nombre = input("Escribe tu nombre: ")
correo = input("Escribe tu correo: ")
contraseña = input("Escribe la contraseña: ")

#creamos el objeto de la clase persona
Persona = persona(id, nombre, correo, contraseña)

def opciones():
    print("Crear usuario")
    print("Eliminar usuario")
    Print("Editar usuario")
    print("Consultar usuario")
    
    

