# Leer el número de llantas de una compra y mostrar el valor que debe pagarse.
# El almacén las vende con la siguiente política: Si se compran menos de 6 llantas,
# el precio unitario es $240000. Si se compran 6 o 7, el precio unitario es $221000,
# y si se compran más de 7 llantas, el precio unitario es $180000.

nro_llantas = int(input("Ingrese numero de llantas a comprar: "))

if nro_llantas < 6:
    valor_total = 240000 * nro_llantas
elif nro_llantas == 6 or nro_llantas == 7:
    valor_total = 221000 * nro_llantas
else:
    valor_total = 180000 * nro_llantas

print(f"El valor de {nro_llantas} llantas es de ${valor_total}")