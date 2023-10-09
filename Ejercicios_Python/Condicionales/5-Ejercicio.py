# ingresar datos
notaUno = float(input("Ingrese nota 1: "))
notaDos = float(input("Ingrese nota 2: "))
notaTres = float(input("Ingrese nota 3: "))

# Calcular promedio
promedio = (notaUno + notaDos + notaTres) / 3

if(promedio >= 3):
    print("Aprobó")
else:
    print(f"No aprobó")