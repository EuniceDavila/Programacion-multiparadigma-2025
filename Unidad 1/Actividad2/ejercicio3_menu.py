print("Menú de operaciones")

while True:
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. Salir")

    opcion = input("Ingresa el número de la opción a elegir (1-4): ")

    if opcion == "1":
        a = float(input("Ingrese un número: "))
        b = float(input("Ingrese otro número: "))
        print(f"El resultado de la suma es: {a + b}")
    elif opcion == "2":
        a = float(input("Ingrese un número: "))
        b = float(input("Ingrese otro número: "))
        print(f"El resultado de la resta es: {a - b}")
    elif opcion == "3":
        a = float(input("Ingrese un número: "))
        b = float(input("Ingrese otro número: "))
        print(f"El resultado de la multiplicación es: {a * b}")
    elif opcion == "4":
        print(" Salió del programa")
        break
    else:
        print("Está opción no es válida")