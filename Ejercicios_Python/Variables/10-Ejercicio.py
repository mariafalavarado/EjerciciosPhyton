salario = 0
diasTrabaj = 0
print("Ingresa el salario")
salario = int(input())
print("Digite la cantidad de días")
diasTrabaj = int(input())
total= salario * diasTrabaj
descuentoPens = total * 0.10
descuentoSalud = total * 0.15

print("El descuento por pension y salud es de:", total - descuentoSalud -descuentoPens)