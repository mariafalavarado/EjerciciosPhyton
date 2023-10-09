# Conversión de temperaturas.
print("1. Convertir Celsius a Fahrenheit")
print("2. Convertir Fahrenheit a Celsius")
print("3. Convertir Kelvin a Celsius")

opcion = input("Ingrese su opción deseada: ")

# realizar la conversión según la opción elegida
if opcion == "1":
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")
elif opcion == "2":
    fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit} grados Fahrenheit son {celsius} grados Celsius.")
elif opcion == "3":
    kelvin = float(input("Ingrese la temperatura en grados Kelvin: "))
    celsius = kelvin - 273.15
    print(f"{kelvin} grados Kelvin son {celsius} grados Celsius.")
else:
    print("Opción inválida. Por favor ingrese una opción del 1 al 3.")
