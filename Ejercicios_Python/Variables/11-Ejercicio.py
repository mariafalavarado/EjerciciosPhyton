numero = 0
contador = 0
numero = int(input("Ingresa un numero: "))

aproximacion = numero / 2.0

# Realizar iteraciones para mejorar la aproximación
for _ in range(1000):
    contador += 1
    aproximacion = 0.5 * (aproximacion + numero / aproximacion)

    # Verificar si la aproximación es lo suficientemente cercana
    cuadrado_aproximacion = aproximacion * aproximacion
    diferencia = cuadrado_aproximacion - numero
    if diferencia < 0:
        diferencia = -diferencia

    if diferencia < 1e-6:
        print(f"La raíz cuadrada de {numero} es aproximadamente {round(aproximacion, 2)}")
        break