# Crea un programa usando funciones y lo que necesites para que el usuario inserte
# N números en una Tupla, después de la captura debe desplegar el siguiente menú
# funcional
# 1. Sumatoria de los elementos de la lista
# 2. Numero mayor de la lista
# 3. Numero menor de la lista
# 4. Promedio
# 5. Moda: es el valor que más se repite de un conjunto de datos
# 6. Rango: es la diferencia entre el valor máximo y el valor mínimo de un
# conjunto de datos

# numeros = (input("ingrese una lista de numeros: "))
# tuple = numeros
# print(tuple)

def main():
    numeros = (input("ingrese una lista de numeros: "))

    while True:
        print("\nSeleccione una opción:")
        print("1. Sumatoria de los elementos de la lista")
        print("2. Número mayor de la lista")
        print("3. Número menor de la lista")
        print("4. Promedio")
        print("5. Moda")
        print("6. Rango")
        print("7. Salir")

        opcion = input("Opción: ")

        if opcion == '1':
            print("Sumatoria de los elementos:", sum(numeros))
        elif opcion == '2':
            print("Número mayor:", max(numeros))
        elif opcion == '3':
            print("Número menor:", min(numeros))
        elif opcion == '4':
            print("Promedio:", sum(numeros) / len(numeros))
        elif opcion == '6':
            print("Rango:", max(numeros) - min(numeros))
        elif opcion == '7':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "":
    main()
