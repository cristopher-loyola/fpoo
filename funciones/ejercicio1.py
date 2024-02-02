# Escribir una función que calcule el total de una factura tras aplicarle
# el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de
# IVA a aplicar, y devolver el total de la factura. Si se invoca la función
# sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

def factura(no_iva, porcentaje_iva=21):
    total = no_iva + (no_iva * porcentaje_iva /100)
    return total
no_iva = float(input("ingresa la cantidad sin iva: "))
porcentaje_persona = input("ingrese el porcentaje del iva: ")
if porcentaje_persona:
    porcentaje_iva = float(porcentaje_persona)
else:
    porcentaje_iva = 21
total = factura(no_iva, porcentaje_iva)
print("El total de la factura es: ", total)