# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
for i in range(1, 11):
    print("tablas de multiplicar", i)
    for a in range (1,11):
        print(i, "x", a, "=", i*a)
    print()