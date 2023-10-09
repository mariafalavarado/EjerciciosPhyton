import math

# Mostrar Menú
print("Seleccione la figura a la que desa calcular el area: ")
print("1. Rectangulo ")
print("2. Cuadrado ")
print("3. Paralelogramo ")
print("4. Rombo ")
print("5. Trapecio ")
print("6. Triangulo ")
print("7. Triangulo Equilatero ")
print("8. Triangulo Rectangulo ")
print("9. Poligono Regular ")

opcion = int(input("Ingrese su opción: "))
print("\n")

if (opcion < 0 or opcion > 9):
    print("Opcion invalida..")
elif (opcion == 1):
    print("***** Area Rectangulo *****")
    ancho = float(input("Ingresar ancho del rectangulo: "))
    largo = float(input("Ingresar largo del rectangulo: "))

    areaRectangulo = ancho * largo
    print(f"El area del rectangulo es {areaRectangulo}")

elif (opcion == 2):
    print("***** Area Cuadrado *****")
    lado = float(input("Ingresar lado del cuadrado: "))

    areaCuadrado = lado * lado
    print(f"El area del cuadrado es {areaCuadrado}")

elif (opcion == 3):
    print("***** Area Paralelogramo *****")
    base = float(input("Ingresar base del Paralelogramo: "))
    altura = float(input("Ingresar altura del Paralelogramo: "))

    areaParalelogramo = base * altura
    print(f"El area del Paralelogramo es {areaParalelogramo}")

elif (opcion == 4):
    print("***** Area Rombo *****")
    diagonalMayor = float(input("Ingresar diagonal mayor del Rombo: "))
    diagonalMenor = float(input("Ingresar diagonal menor del Rombo: "))

    areaRombo = (diagonalMayor * diagonalMenor) / 2
    print(f"El area del Rombo es {areaRombo}")

elif (opcion == 5):
    print("***** Area Trapecio *****")
    baseMayor = float(input("Ingresar base mayor del Trapecio: "))
    baseMenor = float(input("Ingresar base menor del Trapecio: "))
    altura = float(input("Ingresar altura del Trapecio: "))

    areaTrapecio = ( (baseMenor + baseMayor) / 2) * altura
    print(f"El area del Trapecio es {areaTrapecio}")

elif (opcion == 6):
    print("***** Area Triangulo *****")
    base = float(input("Ingresar base del Triangulo: "))
    altura = float(input("Ingresar altura del Triangulo: "))

    areaTriangulo = (base * altura) / 2
    print(f"El area del Triangulo es {areaTriangulo}")

elif (opcion == 7):
    print("***** Area Triangulo Equilatero *****")
    longitud = float(input("Ingresar longitud de un lado del triángulo equilátero: "))

    altura = math.sqrt(longitud ** 2 - (longitud / 2) ** 2)
    areaTrianguloEquilatero = (longitud * altura) / 2

    print(f"El area del Triangulo Equilatero es {areaTrianguloEquilatero}")

elif (opcion == 8):
    print("***** Area Triangulo Rectangulo *****")
    base = float(input("Ingresar base del Triangulo Rectangulo: "))
    altura = float(input("Ingresar altura del Triangulo Rectangulo: "))

    areaTrianguloRectangulo = (base * altura) / 2
    print(f"El area del Triangulo Rectangulo es {areaTrianguloRectangulo}")

elif (opcion == 9):
    print("***** Area Poligono Regular *****")
    numeroLados = float(input("Ingresar el número de lados del polígono regular: "))
    longitud = float(input("Ingresa la longitud de un lado del polígono regular: "))

    areaPoligonoRegular = (numeroLados * longitud ** 2) / (4 * math.tan(math.pi / numeroLados))
    print(f"El area del Poligono Regular es {areaPoligonoRegular}")