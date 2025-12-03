# Función A
def calcular_promedio (numeros):
    return sum(numeros) / len(numeros)

# Función B
contador = 0
def siguiente_id():
    global contador
    contador += 1
    return f"ID-{contador}"

def siguiente_id_puro(contador):
    return f"ID-{contador+1}", contador + 1


# Función C
def agregar_fecha(registro):
    from datetime import datetime
    registro['fecha'] = datetime.now().isoformat()
    return registro

def agregar_fecha_puro(registro, fecha):
    nuevo = registro.copy()
    nuevo['fecha'] = fecha
    return nuevo


# Función D
def filtrar_positivos(numeros):
    return [n for n in numeros if n > 0]

# Función E
import random
def mezclar_lista(lista):
    random. shuffle(lista)
    return lista

import random
def mezclar_lista_pura(lista):
    return random.sample(lista, len(lista))
