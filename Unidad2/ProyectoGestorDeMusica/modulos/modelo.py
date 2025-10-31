"""
modelo.py
Define las clases principales del sistema de gestión de música.
Incluye la clase Cancion y GestorMusica.
"""


class Cancion:
    """
    Representa una canción con título, artista y duración.

    Atributos:
        titulo (str): título de la canción.
        artista (str): nombre del artista o banda.
        duracion (str): duración de la canción en minutos.
    """

    def __init__(self, titulo, artista, duracion):
        """
        Inicializa una instancia de la clase Cancion.
        """
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion

    def __str__(self):
        """Devuelve una representación legible de la canción."""
        return f"{self.titulo} - {self.artista} ({self.duracion} min)"


class GestorMusica:
    """
    Clase que administra una lista de canciones.

    Métodos:
        agregar_cancion(cancion): agrega una nueva canción.
        mostrar_canciones(): muestra todas las canciones.
        buscar_por_artista(artista): busca canciones por nombre de artista.
    """

    def __init__(self):
        """Inicializa el gestor con una lista vacía de canciones."""
        self.canciones = []

    def agregar_cancion(self, cancion):
        """Agrega una nueva canción a la lista."""
        self.canciones.append(cancion)
        print(f"La canción '{cancion.titulo}' fue agregada correctamente.")

    def mostrar_canciones(self):
        """Muestra todas las canciones registradas."""
        if not self.canciones:
            print("No hay canciones en la lista.")
        else:
            print("\nLista de canciones:")
            for i, c in enumerate(self.canciones, start=1):
                print(f"{i}. {c}")

    def buscar_por_artista(self, artista):
        """
        Busca canciones por el nombre del artista.
        
        Parámetros:
            artista (str): nombre del artista a buscar.
        """
        resultados = [c for c in self.canciones if c.artista.lower() == artista.lower()]
        if resultados:
            print(f"\nCanciones de {artista}:")
            for c in resultados:
                print(f"- {c.titulo} ({c.duracion} min)")
        else:
            print(f"No se encontraron canciones del artista '{artista}'.")
