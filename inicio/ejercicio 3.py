Ptry:
    X = int(input("Ingrese un número entero X: "))
except ValueError:
    print("Por favor, ingrese un número entero válido.")
    exit()

suma_total = sum(range(1, X + 1))


print(f"La suma de todos los enteros desde 1 hasta  {X} es: {suma_total}")
