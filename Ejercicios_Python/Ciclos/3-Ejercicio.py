numer = int(input("Ingresa la cantidad de números que deseas mostrar: "))

suma = 0
penultimo = 0
ultimo = 1

if numer >= 1:
    print(penultimo, end=' ')
if numer >= 2:
    print(ultimo, end=' ')

for i in range(2, numer):
    siguiente = penultimo + ultimo
    print(siguiente, end=' ')

    penultimo = ultimo
    ultimo = siguiente

    suma += siguiente

print("\nLa suma de los términos es:", suma)
