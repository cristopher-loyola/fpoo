# 1. Escribir un programa que pida al usuario un número entero positivo y muestre
# por pantalla todos los números impares desde 1 hasta ese número separados
# por comas.

numero = int(input(" introduce un número entero positivo: "))

if numero > 0:
    impares = [str(num) for num in range(1, numero + 1) if num % 2 != 0]
    print("Números impares hasta", numero, ": " + ', '.join(impares))
else:
    print(" introduce un número entero positivo.")
