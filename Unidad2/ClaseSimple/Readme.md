# Proyecto: Clase Libro
### Autor: Eunice Ramona Dávila Lugo

##  Objetivo
Aplicar los fundamentos de Programación Orientada a Objetos (POO) creando una clase, instanciando objetos y manipulando su estado.

##  Diseño de la clase
Elegí los siguientes **atributos** y **métodos** porque representan de forma realista cómo funciona un libro dentro de una biblioteca:

###  Atributos de instancia
- **titulo (str):** para identificar el nombre del libro.
- **autor (str):** para saber quién lo escribió.
- **anio_publicacion (int):** para registrar el año en que fue publicado.
- **prestado (bool):** indica si el libro está prestado o disponible. Se inicializa como `False` porque los libros están disponibles por defecto.

###  Atributo de clase
- **biblioteca (str):** se comparte entre todos los objetos, ya que todos pertenecen a la misma biblioteca (“Biblioteca Central”).

###  Métodos
- **__init__():** inicializa los atributos al crear un nuevo libro.
- **prestar():** cambia el estado del libro a prestado y muestra un mensaje.
- **devolver():** cambia el estado del libro a disponible y muestra un mensaje.
- **mostrar_estado():** imprime toda la información del libro, incluyendo si está prestado o no.

Elegí estos métodos porque permiten **modificar y consultar el estado del objeto**, mostrando el uso básico de la POO.

##  Ejecución del programa
En el archivo `main.py` se crean varios libros populares y se realizan operaciones de préstamo y devolución:

Ejemplo:
```python
libro1 = Libro("Harry Potter y la Piedra Filosofal", "J.K. Rowling", 1997)
libro2 = Libro("Los Juegos del Hambre", "Suzanne Collins", 2008)
libro3 = Libro("Maze Runner: Correr o Morir", "James Dashner", 2009)

libro1.prestar()
libro2.prestar()
libro2.devolver()

libro1.mostrar_estado()
libro2.mostrar_estado()
libro3.mostrar_estado()
