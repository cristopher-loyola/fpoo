numero = int(input("ingrese un numero: "))

i = numero - 1
a= 1

while i >= 0:
    print(' ' * i + '*' * a + ' ' * i)
    a += 2
    i -= 1