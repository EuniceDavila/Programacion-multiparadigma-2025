"""Aquí yo implementé funciones simples para guardar y cargar JSON
 No usé bases de datos"""

import json
from typing import List, Dict

def guardar_json(ruta: str, lista: List[Dict])-> None:
    """Guardo una lista de diccionarios en la ruta indicada
    Yo prefiero usar indent=2 para que sea más legible al abrir el archivo"""
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(lista, f, ensure_ascii=False, indent=2)

def cargar_json(ruta: str)-> List[Dict]:
    """Cargo y devuelvo la lista de diccionarios desde el archivo JSON
    Si ocurre un error (archivo no existe o contenido inválido), devuelvo una lista vacía"""
    
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return[]