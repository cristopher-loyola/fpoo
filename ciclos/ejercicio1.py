entero = int(input("ingresa un numero entero positivo: ")) 
        
suma = 0
for num in range(1,entero):
    if num % 2 != 0:
        suma += num
    print(f"la suma de los numeros pares del 1 al 10 e:  {suma} ")