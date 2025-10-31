"""
main.py
Archivo principal que controla el flujo del programa.
Permite al usuario agregar, listar y buscar canciones.
"""

from modulos.modelo import Cancion, GestorMusica
from modulos.utilidades import limpiar_pantalla, mostrar_menu


def main():
    """
    Función principal del programa.
    Controla las opciones del menú y llama a las funciones del gestor.
    """
    gestor = GestorMusica()

    while True:
        limpiar_pantalla()
        opcion = mostrar_menu()

        if opcion == "1":
            titulo = input("Ingrese el título de la canción: ")
            artista = input("Ingrese el artista: ")
            duracion = input("Ingrese la duración (en minutos): ")
            cancion = Cancion(titulo, artista, duracion)
            gestor.agregar_cancion(cancion)

        elif opcion == "2":
            gestor.mostrar_canciones()

        elif opcion == "3":
            artista = input("Ingrese el nombre del artista: ")
            gestor.buscar_por_artista(artista)

        elif opcion == "4":
            print("Saliendo del sistema de música...")
            break

        else:
            print("Opción no válida.")

        input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()
