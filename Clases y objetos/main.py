from personaje import *
from armas import *

#solicitar datos Spartan
print("===Datos del Guerrero===")
nombreS= input("Escribe el nombre del spartan: ")
especieS= input("Escribe la especie de tu spartan: ")
alturaS= float(input("Escribe la altura del spartan: "))
#solicitar datos del nemesis
print("===Datos del Nemesis===")
nombreN= input("Escribe el nombre del nemesis: ")
especieN= input("Escribe la especie de tu nemesis: ")
alturaN= float(input("Escribe la altura del nemesis: "))

#Creamos el objeto de la clase personaje    
spartan = personaje(especieS,nombreS,alturaS)
nemesis = personaje(especieN,nombreN,alturaN)
arma=armas()
print("Datos del spartan: ")
print(spartan.nombre)
print(spartan.especie)
print(spartan.altura)

print("Datos del nemesis: ")
print(nemesis.nombre)
print(nemesis.especie)
print(nemesis.altura)
#usamos los metoso del spartan
spartan.correr(True)
spartan.lanzarGranada()

print("====Metodos del nemesis====")
nemesis.correr(True)
nemesis.lanzarGranada()
#usamos los metodos del arma
arma.seleccionarArma(spartan.nombre)
arma.recargarArma(65)