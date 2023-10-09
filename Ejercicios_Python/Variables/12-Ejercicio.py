# Solicita al usuario que ingrese la longitud de los catetos
cateto1 = float(input("Ingresa la longitud del primer cateto: "))
cateto2 = float(input("Ingresa la longitud del segundo cateto: "))

# Calcula la hipotenusa utilizando el Teorema de Pitágoras
hipotenusa = (cateto1**2 + cateto2**2)**0.5

# Imprime el resultado
print(f"La hipotenusa es: {hipotenusa}")