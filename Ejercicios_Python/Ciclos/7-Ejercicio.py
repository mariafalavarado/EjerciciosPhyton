cont = 1
x = 1

for columna in range(1, 6):
    for fila in range(1, cont + 1):
        print(x, end='')
        x = x + 1
    
    cont = cont + 1
    x = 1
    print()  # Imprime una nueva línea al final de cada fila


