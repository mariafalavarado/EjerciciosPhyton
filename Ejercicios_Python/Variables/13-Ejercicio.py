# ingresar valor en segundos
segundos = int(input("Digite tiempo en segundos : "))

# Formula para convertir a horas
horas = segundos / 3600

# Formula para convertir a minutos
minutos = segundos / 60

# Mostrar mensaje
print(f"{segundos} segundos equivale a {horas} horas")
print(f"{segundos} segundos equivale a {minutos} minutos")