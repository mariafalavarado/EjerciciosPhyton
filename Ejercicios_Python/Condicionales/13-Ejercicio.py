peso = float(input("Ingrese su peso en Kilos KG: "))
estatura = float(input("Ingrese su estatura en metros M: "))

imc = peso / (estatura * estatura)

if imc < 18.5:
    print("Desnutrido")
elif imc >= 18.5 and imc < 25:
    print("Normal")
elif imc >= 25 and imc < 30:
    print("Sobrepeso")
elif imc >= 30 and imc < 35:
    print("Obesidad Grado 1")
elif imc >= 35 and imc <= 40:
    print("Obesidad Grado 2")
elif imc > 40:
    print("Obesidad Grado 3")