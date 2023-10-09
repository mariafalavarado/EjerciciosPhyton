factorial = 1

num = int(input("Digite un número para calcular el factorial: "))

for i in range(1, num + 1):
    factorial = factorial * i

print(f"El factorial de {num} es {factorial}")
