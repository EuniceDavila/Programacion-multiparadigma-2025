"""Aqui implemente las clases principales
"""
from typing import Dict, List

class Persona:
    """Yo implementé la clase Persona porque quería tener una base común para futuros roles 
    Atributos:
    nombre (str): Nombre completo de la persona"""
    
    def __init__(self, nombre: str):
        """Inicializo una Persona con su nombre
        Yo agregué este constructor simple para mantener las cosas claras"""
        self.nombre = nombre
    
    def __str__(self) -> str:
        return self.nombre

class Estudiante(Persona):
    """Yo implementé Estudiante heredando de Persona para demostrar herencia
    Atributos:
    nombre (str): nombre del estudiante
    id_estudiante (str): identificador único
    calificaciones (Dict[str, List[float]]): mapa asignatura -> lista de notas"""
    
    def __init__(self, nombre: str, id_estudiante: str):
        super().__init__(nombre)
        self.id_estudiante = id_estudiante
        self.calificaciones: Dict[str, List[float]] = {}
        
    def agregar_asignatura(self, asignatura: str) -> None:
        """Agrego una asignatura vacia si no existe
        Yo agregué esto para que sea sencillo registrar notas después"""
        if asignatura not in self.calificaciones:
            self.calificaciones[asignatura] = []
    
    def registrar_nota(self, asignatura: str, nota: float) -> None:
        """Registro una nota en la asignatura indicada
        Yo hice validaciones mínimas como que la nota debe estar entre 0 y 100"""
        if nota < 0 or nota > 100:
            raise ValueError("La nota debe estar entre 0 y 100")
        self.agregar_asignatura(asignatura)
        self.calificaciones[asignatura].append(float(nota))
    
    def promedio_asignatura(self, asignatura: str) -> float:
        """Devuelvo el promedio de una asignatura o 0.0 si no hay notas
        Yo implementé este método para calcular promedios por materia"""
        notas = self.calificaciones.get(asignatura, [])
        if not notas:
            return 0.0
        return sum(notas) / len(notas)
    
    def promedio_general(self) -> float:
        """Devuelvo el promedio general del estudiante
        Si no hay notas devuelvo 0.0"""
        todas = []
        for notas in self.calificaciones.values():
            todas.extend(notas)
        if not todas:
            return 0.0
        return sum(todas) / len(todas)
    
    def a_diccionario(self) -> Dict:
        """Serializo el estudiante a un diccionario para guardar"""
        return {
            "nombre": self.nombre,
            "id_estudiante": self.id_estudiante,
            "calificaciones": self.calificaciones,
            }
        
    @staticmethod
    def desde_diccionario(d: Dict) -> 'Estudiante':
        """Creo un Estudiante desde un diccionario 
        Implementé esto para facilitar la recuperación desde JSON"""
        e = Estudiante(d["nombre"], d["id_estudiante"])
        e.calificaciones = {k: list(v) for k, v in d.get("calificaciones",
    {}).items()}
        return e