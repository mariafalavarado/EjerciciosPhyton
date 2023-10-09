suma = 0

for i in range(1, 11):
    numero = int(input("Ingrese un número: "))
    suma = numero + suma

promedio = suma / 10
print(f"La suma de los numeros ingresados es {suma} y el promedio es {promedio}")