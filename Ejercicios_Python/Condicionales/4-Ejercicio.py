# ingresar datos
numeroUno = int(input("Ingrese primer número: "))
numeroDos = int(input("Ingrese segundo número: "))

if(numeroUno == numeroDos):
    print("Los números ingresados son iguales")
elif (numeroUno > numeroDos):
    print(f"Número uno {numeroUno} es mayor al número 2 {numeroDos}")
else:
    print(f"Número dos {numeroDos} es mayor al número 1 {numeroUno}")