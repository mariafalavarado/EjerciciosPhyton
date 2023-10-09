# El precio que debe pagar un cliente por una pizza depende del tamaño seleccionado, como se muestra a continuación:
# 1 - $15.000
# 2 - 24.000
# 3 - 36.000
#
# Si cada ingrediente adicional cuesta $4.000.
# Escribir un programa que solicite al empleado encargado de registrar las ventas,
# el tamaño de la pizza y el número de ingredientes adicionales y muestre al cliente el precio que debe pagar.

print("..... Tabla de precios .....")
print("1 - $15.000")
print("2 - $24.000")
print("3 - $36.000")

tamanio = int(input("Digite el tamaño de la pizza que desea comprar: "))

print("Ingredientes adicionales por $4.000 cada uno")

nro_ingredientes = int(input("Ingrese la cantidad de ingredientes adicionales deseados: "))

if tamanio == 1:
    precio_base = 15000
elif tamanio == 2:
    precio_base = 24000
elif tamanio == 3:
    precio_base = 36000
else:
    precio_base = 0

if precio_base > 0:
    precio_total = precio_base + (nro_ingredientes * 4000)
    print(f"La pizza {tamanio} cuesta ${precio_base} más {nro_ingredientes} ingredientes, el valor total a pagar es ${precio_total}")
else:
    print("Tamaño de pizza no válido. Por favor, elija un tamaño válido (1, 2 o 3).")
