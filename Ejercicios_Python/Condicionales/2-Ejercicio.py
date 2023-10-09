# ingresar datos
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

if(edad >= 18 and edad <= 100):
    print("Usted es mayor de edad")
elif (edad >= 0 and edad < 18):
    print("Usted es menor de edad")
else:
    print("ingresar una edad válida")
    