# Fundamentos de Programación Funcional

## Autora:
#### Eunice Ramona Dávila Lugo

## Parte 1: Identificación y Análisis
## Función A
```python
def calcular_promedio(numeros):  
  return sum(numeros) / len(numeros) 
  ```

#### ¿Es pura?
Esta función sí es pura.

#### ¿Por qué?
Yo entiendo que no cambia nada fuera de la función y siempre devuelve el mismo resultado si le paso la misma lista. Por eso considero que cumple con las características de una función pura.

#### ¿Cómo la haría pura?
Ya es pura, así que no es necesario modificarla.

## Función B
```python
contador = 0
def siguiente_id():  
    global contador  
    contador += 1  
    return f"ID-{contador}"
```


#### ¿Es pura?
Esta función es impura.

#### ¿Por qué?
Porque esta función modifica una variable global llamada contador. Como depende de un estado externo y cambia cada vez que se ejecuta, opino que no es pura.

#### ¿Cómo la haría pura?
La forma más correcta de volverla pura es evitar el uso del estado global y pasar el contador como parámetro, devolviendo el nuevo valor sin modificar nada afuera.

#### Versión pura
```python
def siguiente_id_puro(contador):  
    return f"ID-{contador+1}", contador + 1
```

## Función C
```python
def agregar_fecha(registro):  
    from datetime import datetime  
    registro['fecha'] = datetime.now().isoformat()  
    return registro
```

#### ¿Es pura?
Esta función es impura.

#### ¿Por qué?
Por dos razones. Primero, modifica el diccionario original, lo cual es una mutación y segundo, usa datetime.now(), y eso hace que la salida cambie cada vez.

#### ¿Cómo la haría pura?
La solución es no modificar el objeto original y permitir que la fecha llegue como parámetro.

#### Versión pura
```python
def agregar_fecha_puro(registro, fecha):  
    nuevo = registro.copy()  
    nuevo['fecha'] = fecha  
    return nuevo
```

## Función D
```python
def filtrar_positivos(numeros):  
    return [n for n in numeros if n > 0]
```

#### ¿Es pura?
Es pura.

#### ¿Por qué?
Por lo que veo, la función no altera la lista original y siempre produce la misma salida con la misma entrada, no presenta efectos secundarios.

#### ¿Cómo la haría pura?
No es necesario cambiarla porque ya es pura.

## Función E
```python
import random  
def mezclar_lista(lista):  
    random.shuffle(lista)  
    return lista
```

#### ¿Es pura?
Esta función es impura.

#### ¿Por qué?
random.shuffle modifica la lista original (mutación). Además, al usar aleatoriedad, yo opino que nunca va a producir el mismo resultado con la misma entrada, lo que la hace impura.

#### ¿Cómo la haría pura?
La mejor opción de convertirla en una función pura es devolver una nueva lista mezclada sin cambiar la original.

#### Versión pura
```python
import random  
def mezclar_lista_pura(lista):  
    return random.sample(lista, len(lista))
```