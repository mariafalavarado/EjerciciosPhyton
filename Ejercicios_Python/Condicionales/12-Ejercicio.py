# Un local vende sus productos con la siguiente promoción.
# Si compra hasta 5 artículos, no hay descuento.
# Si compra más de 5 artículos, pero menos de 10, el precio unitario se reduce en 5%.
# Si compra 10 o más artículos, el precio unitario se reduce en 8%.
# Ingrese un dato de cantidad y el valor del precio unitario original.
# Calcule y muestre el valor total a pagar.

nro_articulos = int(input("Ingrese la cantidad de artículos a comprar: "))
vlr_unitario_articulos = float(input("Ingrese el valor por unidad de los artículos: "))

if nro_articulos <= 5:
    valor_total = nro_articulos * vlr_unitario_articulos
    print(f"El valor total a pagar es ${valor_total}")
elif nro_articulos < 10:
    descuento = 0.05  # 5% de descuento
    valor_total = nro_articulos * vlr_unitario_articulos * (1 - descuento)
    print(f"El valor total a pagar con 5% de descuento es ${valor_total}")
else:
    descuento = 0.08  # 8% de descuento
    valor_total = nro_articulos * vlr_unitario_articulos * (1 - descuento)
    print(f"El valor total a pagar con 8% de descuento es ${valor_total}")