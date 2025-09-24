tareas = []  

while True:
    print("\nGestor de Tareas")
    print("\n1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

    opcion = input("\nElige una opción: ")

    if opcion == "1":
        nueva = input("Escribe tu tarea: ")
        tareas.append(nueva + " [Pendiente]")
        print("\nTarea agregada.")

    elif opcion == "2":
        if len(tareas) == 0:
            print("\nNo tienes tareas.")
        else:
            print("\n--- Tareas actuales ---")
            for i in range(len(tareas)):
                print(f"{i+1}. {tareas[i]}")

    elif opcion == "3":
        if len(tareas) == 0:
            print("\nNo hay tareas para marcar.")
        else:
            num = int(input("\nNúmero de la tarea a marcar: "))
            if 1 <= num <= len(tareas):
                tareas[num-1] = tareas[num-1].replace("[Pendiente]", "[Completada]")
                print("\nTarea marcada como completada")
            else:
                print("\nNúmero inválido")

    elif opcion == "4":
        if len(tareas) == 0:
            print("\nNo hay tareas para eliminar")
        else:
            num = int(input("\nNúmero de la tarea a eliminar: "))
            if 1 <= num <= len(tareas):
                eliminada = tareas.pop(num-1)
                print(f"\nTarea: '{eliminada}' eliminada.")
            else:
                print("\nNúmero inválido")

    elif opcion == "5":
        print("\nSaliendo del gestor de tareas")
        break

    else:
        print("\nOpción no válida")