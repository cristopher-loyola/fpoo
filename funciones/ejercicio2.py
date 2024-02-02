# Escribir una función que calcule el área de un círculo y otra que
# calcule el volumen de un cilindro usando la primera función.

import math
 
def area(radio):
     return math.pi*(radio**2)
def volumen(radio, altura):
    return area(radio) * altura
radio = float(input("cual es el radio?"))
altura_cilindro = float(input("cual es la altura del cilindro?"))

print(f"El area del circulo es:{area(radio)}")
print(f"El volumen del cilindro es: {volumen(radio,altura_cilindro)}")
    