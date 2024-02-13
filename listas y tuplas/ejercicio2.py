# b. Crea un programa que llene una lista de 30 valores aleatorios en un rango del 10
# al 20, con la lista llena el usuario podrá
# a. Contar número repetidos
# b. Eliminar numero repetidos
# c. Remplazar los repetidos con 0
def obtener_numeros():
    numeros = []
    for _ in range(30):
        while True:
            try:
                num = int(input("Ingrese un número entre 10 y 20: "))
                if 10 <= num <= 20:
                    numeros.append(num)
                    break
                else:
                    print("El número debe estar en el rango del 10 al 20.")
            except ValueError:
                print("Ingrese un número válido.")
    return numeros

def contar_repetidos(numeros):
    contador = {}
    for num in numeros:
        if num in contador:
            contador[num] += 1
        else:
            contador[num] = 1
    return contador

def eliminar_repetidos(numeros):
    return list(set(numeros))

def reemplazar_repetidos_con_cero(numeros):
    contador = contar_repetidos(numeros)
    for i in range(len(numeros)):
        if contador[numeros[i]] > 1:
            numeros[i] = 0
            contador[numeros[i]] -= 1
    return numeros

def main():
    numeros = obtener_numeros()
    print("Lista ingresada:", numeros)

    while True:
        print("\nSeleccione una opción:")
        print("a. Contar números repetidos")
        print("b. Eliminar números repetidos")
        print("c. Reemplazar números repetidos con 0")
        print("d. Salir")

        opcion = input("Opción: ").lower()

        if opcion == 'a':
            contador = contar_repetidos(numeros)
            print("Número repetido: Frecuencia")
            for num, freq in contador.items():
                print(num, ":", freq)
        elif opcion == 'b':
            lista_sin_repetidos = eliminar_repetidos(numeros)
            print("Lista sin números repetidos:", lista_sin_repetidos)
        elif opcion == 'c':
            lista_reemplazada = reemplazar_repetidos_con_cero(numeros.copy())
            print("Lista con números repetidos reemplazados por 0:", lista_reemplazada)
        elif opcion == 'd':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
