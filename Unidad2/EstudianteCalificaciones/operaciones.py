"""Funciones para gestionar la lista de estudiantes y sus calificaciones"""
 
from typing import Dict, List
from modelos import Estudiante
import datos

class GestorEstudiantes:
    """Yo implementé esta clase para agrupar operaciones sobre estudiantes"""
    
    def __init__(self):
        self.estudiantes: Dict[str, Estudiante] = {}
    
    def agregar_estudiante(self, estudiante: Estudiante)-> None:
        """Agrego un estudiante por su id
        Si el id ya existe lanzo un ValueError para evitar duplicados"""
        if estudiante.id_estudiante in self.estudiantes:
            raise ValueError("Ya existe un estudiante con ese ID")
        self.estudiantes[estudiante.id_estudiante] = estudiante
   
    def listar_estudiantes(self)-> List[Estudiante]:
        """Devuelvo la lista de estudiantes ordenada por nombre
        Yo prefiero ordenar por nombre"""
        return sorted(self.estudiantes.values(), key=lambda s: s.nombre)
   
    def obtener_estudiante(self, id_estudiante: str)-> Estudiante:
        """Devuelvo el estudiante por ID o lanzo KeyError si no existe"""
        if id_estudiante not in self.estudiantes:
            raise KeyError("Estudiante no encontrado.")
        return self.estudiantes[id_estudiante]
    
    def registrar_nota(self, id_estudiante: str, asignatura: str, nota: float)-> None:
        """Registro una nota en un estudiante específico"""
        est = self.obtener_estudiante(id_estudiante)
        est.registrar_nota(asignatura, nota)
    
    def resumen_estudiante(self, id_estudiante: str)-> Dict:
        """Genero un resumen con los datos del estudiante
        Incluye nombre, id, calificaciones y promedio general"""
        est = self.obtener_estudiante(id_estudiante)
        return {
            "nombre": est.nombre,
            "id_estudiante": est.id_estudiante,
            "calificaciones": est.calificaciones,
            "promedio_general": est.promedio_general(),
            }
    
    def guardar(self, ruta: str)-> None:
        """Guardo todos los estudiantes en un archivo JSON"""
        lista = [e.a_diccionario() for e in self.estudiantes.values()]
        datos.guardar_json(ruta, lista)
        
    def cargar(self, ruta: str)-> None:
        """Cargo estudiantes desde un archivo JSON
        Si el archivo no existe dejo la lista vacía"""
        lista = datos.cargar_json(ruta)
        self.estudiantes = {}
        for d in lista:
            e = Estudiante.desde_diccionario(d)
            self.estudiantes[e.id_estudiante] = e