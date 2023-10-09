tamanio_z = 7

for i in range(1, tamanio_z + 1):
    for j in range(tamanio_z, 0, -1):
        if i == 1 or i == tamanio_z:
            print("*", end='')
        elif i == j:
            print("*", end='')
        else:
            print(" ", end='')
    
    print()  # Imprime una nueva línea al final de cada fila
