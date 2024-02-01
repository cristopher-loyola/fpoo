# 2. Escribir un programa que pida al usuario un número entero positivo y muestre
# por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
entero = int(input("ingrese un numero entero: "))

for atras in range (entero, -1, -1):
    if atras == 0:
        print(atras)
    else:
        print(atras, end=",")