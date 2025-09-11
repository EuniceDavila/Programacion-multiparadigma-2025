import math

print("Figuras")
print("1. Triángulo")
print("2. Cuadrado")
print("3. Círculo")

opcion = input("Seleccione el número de la figura a la cual desea calcular su área (1,2 ó 3): ")

if opcion == "1":
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area = (base * altura) / 2
    print(f"El área del triángulo es: {area}")
elif opcion == "2":
    lado = float(input("Ingrese el lado del cuadrado: "))
    area = lado * lado
    print(f"El área del cuadrado es: {area}")
elif opcion == "3":
    radio = float(input("Ingrese el radio del círculo: "))
    area = math.pi * (radio ** 2)
    print(f"El área del círculo es: {area}")
else:
    print("Está opción no es válida")