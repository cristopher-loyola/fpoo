from personaje import *
from armas import *
#Creamos el objeto de la clase personaje    
spartan = personaje()
arma=armas()

print(spartan.nombre)
print(spartan.especie)
print(spartan.altura)

#usamos los metoso del spartan
spartan.correr(True)
spartan.lanzarGranada()


#usamos los metodos del arma
arma.seleccionarArma(spartan.nombre)
arma.recargarArma(65)