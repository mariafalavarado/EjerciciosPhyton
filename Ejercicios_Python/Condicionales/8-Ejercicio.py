# Solicitar tres números al usuario e imprimirlos en orden ascendente y descendente.

num1 = float(input("Ingrese numero 1: "))
num2 = float(input("Ingrese numero 2: "))
num3 = float(input("Ingrese numero 3: "))

# Ordenar los números en forma ascendente
print("Orden ascendentes")
if num1 < num2 < num3:
    print(num1, "-", num2, "-", num3)
elif num1 < num3 < num2:
    print(num1, "-", num3, "-", num2)
elif num2 < num1 < num3:
    print(num2, "-", num1, "-", num3)
elif num2 < num3 < num1:
    print(num2, "-", num3, "-", num1)
elif num3 < num1 < num2:
    print(num3, "-", num1, "-", num2)
else:
    print(num3, "-", num2, "-", num1)

# Ordenar los números en forma descendente
print("\n Orden descendentes")
if num1 > num2 > num3:
    print(num1, "-", num2, "-", num3)
elif num1 > num3 > num2:
    print(num1, "-", num3, "-", num2)
elif num2 > num1 > num3:
    print(num2, "-", num1, "-", num3)
elif num2 > num3 > num1:
    print(num2, "-", num3, "-", num1)
elif num3 > num1 > num2:
    print(num3, "-", num1, "-", num2)
else:
    print(num3, "-", num2, "-", num1)