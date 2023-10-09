# Programa que permite a un usuario tomar una decisión del tipo de pago a usar.
# Si la cuenta es menor a $150000 pago en efectivo.
# Si es de $150000 hasta $300000 pago con el celular (dinero electrónico).
# Si es mayor a $300000 hasta $600000, pago con la tarjeta de débito.
# Caso contrario, pago con la tarjeta de crédito.

valor_cuenta = float(input("Ingrese el valor de la cuenta a pagar: "))

if valor_cuenta < 150000:
    print("Pagar en Efectivo")
elif 150000 <= valor_cuenta <= 300000:
    print("Pagar con el celular (dinero electrónico)")
elif 300000 < valor_cuenta <= 600000:
    print("Pagar con la tarjeta de débito")
else:
    print("Pagar con la tarjeta de crédito")