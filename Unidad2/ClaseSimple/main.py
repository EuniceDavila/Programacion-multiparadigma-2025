from libro import Libro

libro1 = Libro("Harry Potter y la Piedra Filosofal", "J.K. Rowling", 1997)
libro2 = Libro("Los Juegos del Hambre", "Suzanne Collins", 2008)
libro3 = Libro("Maze Runner: Correr o Morir", "James Dashner", 2009)
libro4 = Libro("Percy Jackson y el Ladrón del Rayo", "Rick Riordan", 2005)


libro1.prestar()

libro2.prestar()

libro2.mostrar_estado()

libro2.devolver()

libro2.mostrar_estado()

libro1.mostrar_estado()

libro3.mostrar_estado()

libro4.mostrar_estado()
libro4.prestar()
libro4.mostrar_estado()
libro4.devolver()
libro4.mostrar_estado()