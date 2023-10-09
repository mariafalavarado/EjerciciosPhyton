edad = int(input("Ingrese su edad: "))
genero = int(input("Ingrese su género (1 - femenino, 2 - masculino): "))

# Calcular el número de pulsaciones según el género
if genero == 1:
    pulsaciones = (220 - edad) / 10
elif genero == 2:
    pulsaciones = (210 - edad) / 10
else:
    print("Género no válido. Por favor, ingrese 1 para femenino o 2 para masculino.")

# Mostrar el número de pulsaciones si el género es válido
if pulsaciones == 1 or pulsaciones == 2:
    print(f"El número de pulsaciones por cada 10 segundos de ejercicio aeróbico es: {pulsaciones}")