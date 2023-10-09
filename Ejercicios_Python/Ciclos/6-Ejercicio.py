alto = 9
cont = 1

for columna in range(1, alto + 1):
    for fila in range(1, cont + 1):
        print("* ", end=' ')
    
    if columna < 5:
        cont = cont + 1
    else:
        cont = cont - 1

    print()  # Imprime una nueva línea al final de cada fila

