edad = int(input("Ingresa tu edad: "))

if edad < 4:
    print("Puede entrar gratis")
elif edad <= 18:
    print("Debe pagar 110")
else:
    print("Debe pagar 190")