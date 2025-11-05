"""Interfaz por consola para usar el sistema
Diseñé un menú sencillo para poder probar las funciones"""

from operaciones import GestorEstudiantes
from modelos import Estudiante

RUTA_DATOS = "datos.json"

def menu():
    gestor = GestorEstudiantes()
    gestor.cargar(RUTA_DATOS)
    
    while True:
        print("\n------- Sistema de Estudiantes y Calificaciones -------")
        print("1. Agregar estudiante")
        print("2. Registrar nota")
        print("3. Listar estudiantes")
        print("4. Ver resumen de estudiante")
        print("5. Guardar y salir")
        print("0. Salir sin guardar")
        opc = input("Elige una opción: ")
        
        if opc == "1":
            nombre = input("\nNombre del estudiante: ")
            id_est = input("ID del estudiante: ")
            
            try:
                gestor.agregar_estudiante(Estudiante(nombre, id_est))
                print("Estudiante agregado correctamente")
            except ValueError as e:
                print("Error:", e)
        
        elif opc == "2":
            id_est = input("\nID del estudiante: ")
            asignatura = input("Asignatura: ")
            try:
                nota = float(input("Nota (0-100): "))
                gestor.registrar_nota(id_est, asignatura, nota)
                print("Nota registrada exitosamente")
            except Exception as e:
                print("Error:", e)
        elif opc == "3":
            estudiantes = gestor.listar_estudiantes()
            
            if not estudiantes:
                print("\nNo hay estudiantes registrados")
            for e in estudiantes:
                print(f"\n- {e.id_estudiante}: {e.nombre} (Promedio:{e.promedio_general():.2f})")
        
        elif opc == "4":
            id_est = input("\nID del estudiante: ")
            try:
                resumen = gestor.resumen_estudiante(id_est)
                print("\n========== Resumen del estudiante ==========")
                print("Nombre:", resumen["nombre"])
                print("ID:", resumen["id_estudiante"])
                print("Calificaciones:")
                califs = resumen["calificaciones"]
                if not califs:
                    print(" (No hay calificaciones registradas)")
                    
                else:
                    for mat, notas in califs.items():
                        avg = sum(notas) / len(notas) if notas else 0.0
                        print(f" - {mat}: notas={notas} promedio={avg:.2f}")
                print(f"Promedio general: {resumen['promedio_general']:.2f}")
            except KeyError as e:
                print("Error: estudiante no encontrado.")
            except Exception as e:
                print("Error inesperado:", e)
        
        elif opc == "5":
            gestor.guardar(RUTA_DATOS)
            print("\nDatos guardados en", RUTA_DATOS)
            break
        
        elif opc == "0":
            print("\nSaliendo sin guardar")
            break
        
        else:
            print("\nOpción no válida")
            
if __name__ == "__main__":
    menu()