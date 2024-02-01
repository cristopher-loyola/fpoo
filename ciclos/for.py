# palabra = input("imgrese una palabra:")
# contador_vocales = 0
# for letra in palabra:
#     if letra in palabra:
#         if letra.lower() in "aeiou":
#             contador_vocales += 1
            
# print(f"la palabra '(palabra)' tiene (contador_vocales) vocal(es). ")

suma = 0
for num in range(1, 11):
    if num % 2 == 0:
        suma += num
        print(f"La suma de los numeros pares del 1 al 10 es: {suma}")