tamanio_piramide = 4
contador = 0

for i in range(1, tamanio_piramide + 1):
    for j in range(1, tamanio_piramide + 1):
        if i == 1:
            if j == 3:
                contador += 1
                print(contador, end='')
            else:
                print(" ", end='')
        elif i == 2:
            if j == 2 or j == 3:
                contador += 1
                print(contador, end='')
            else:
                print(" ", end='')
        elif i == 3:
            if j != 1:
                contador += 1
                print(contador, end='')
            else:
                print(" ", end='')
        elif i == 4:
            contador += 1
            print(contador, end='')

    print()  # Imprime una nueva línea al final de cada fila
cont = 1
x = 1

for columna in range(1, 6):
    for fila in range(1, cont + 1):
        print(x, end='')
        x = x + 1
    
    cont = cont + 1
    x = 1
    print()  # Imprime una nueva línea al final de cada fila


