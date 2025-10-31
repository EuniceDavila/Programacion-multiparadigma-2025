"""
utilidades.py
Contiene funciones auxiliares para mejorar la experiencia del usuario.
"""

import os


def limpiar_pantalla():
    """
    Limpia la pantalla de la consola.
    Compatible con Windows, macOS y Linux.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_menu():
    """
    Muestra el menú principal del programa y devuelve la opción elegida.
    
    Retorna:
        str: opción seleccionada por el usuario.
    """
    print("----GESTOR DE MÚSICA----")
    print("1. Agregar canción")
    print("2. Mostrar canciones")
    print("3. Buscar canciones por artista")
    print("4. Salir")
    return input("Seleccione una opción: ")
