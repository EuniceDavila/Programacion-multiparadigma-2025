class Producto:
    def __init__(self, nombre: str, precio: float):
       
        if not nombre or not isinstance(nombre, str):
            raise ValueError("Nombre inválido")
        if not isinstance(precio, (int, float)) or precio <= 0:
            raise ValueError("Precio debe ser mayor que 0")

        self.nombre = nombre
        self.__stock = 0
        self._precio = float(precio)

    @property
    def stock(self) -> int:
        # Getter del stock
        return self.__stock

    @stock.setter
    def stock(self, value: int):
        #  no permite valores negativos
        if not isinstance(value, int):
            raise ValueError("El stock debe ser un entero")
        if value < 0:
            raise ValueError("El stock no puede ser negativo")
        self.__stock = value

    @property
    def precio(self) -> float:
        # Getter del precio
        return self._precio

    @precio.setter
    def precio(self, value: float):
       
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("El precio debe ser mayor que 0")
        self._precio = float(value)

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Precio: ${self._precio:.2f}, Stock: {self.__stock}"

    def __eq__(self, other) -> bool:
     
        if not isinstance(other, Producto):
            return False
        return self.nombre.strip().lower() == other.nombre.strip().lower()