# ingresar valor en metros
metros = float(input("Digite distancia en metros : "))

# Formula para convertir a Kilometros
kilometros = metros / 1000

# Formula para convertir a centimetros
centimetros = metros * 100

# Formula para convertir a milimetros
milimetros = metros * 1000

# Mostrar mensaje
print(f"{metros} metros equivale a {kilometros} kilometros")
print(f"{metros} metros equivale a {centimetros} centimetros")
print(f"{metros} metros equivale a {milimetros} milimetros")