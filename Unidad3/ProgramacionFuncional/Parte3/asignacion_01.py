#   Programación Funcional - Parte 3
#   Autora: Eunice Ramona Dávila Lugo

#  crear_transformador

def crear_transformador(funcion):
    """
    Yo entiendo que esta función recibe una transformación (funcion)
    y devuelve otra función que aplica esa transformación a cada
    elemento de una lista, sin modificar la lista original
    """
    def transformador(lista):
        return [funcion(x) for x in lista]
    return transformador

# crear_filtro

def crear_filtro(predicado):
    """
    Esta función recibe un predicado (algo que devuelve True/False)
    y regresa una función que filtra una lista basándose en ese predicado
    """
    def filtro(lista):
        return [x for x in lista if predicado(x)]
    return filtro

# crear_reductor

def crear_reductor(funcion, valor_inicial):
    """
    Esta función imita la operación reduce:
    toma una función acumuladora y un valor inicial, y genera
    una nueva función que reduce toda la lista a un único valor
    """
    def reductor(lista):
        acumulador = valor_inicial
        for x in lista:
            acumulador = funcion(acumulador, x)
        return acumulador
    return reductor

# componer

def componer(*funciones):
    """
    Esta función recibe varias funciones y regresa una función que
    aplica todas en orden (izquierda a derecha). Yo lo veo como
    construir un pipeline de pasos
    """
    def compuesto(valor):
        resultado = valor
        for f in funciones:
            resultado = f(resultado)
        return resultado
    return compuesto


numeros = [1, -2, 3, -4, 5, -6, 7, 8, -9, 10]

pipeline = componer(
    crear_filtro(lambda x: x > 0),
    crear_transformador(lambda x: x ** 2),
    crear_reductor(lambda acc, x: acc + x, 0)
)

resultado = pipeline(numeros)

print(f"Resultado: {resultado}") 
