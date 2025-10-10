from producto import Producto
from typing import Optional, Dict

class Inventario:
    def __init__(self):
        # Diccionario privado: keys -> nombre en minúsculas, values -> Producto
        self.__productos: Dict[str, Producto] = {}

    def agregar_producto(self, producto: Producto):
        # Agrega un producto nuevo o actualiza uno existente
        if not isinstance(producto, Producto):
            raise ValueError("Se debe pasar un objeto Producto")

        key = producto.nombre.strip().lower()
        if key in self.__productos:
            existente = self.__productos[key]
            existente.stock = existente.stock + producto.stock
            existente.precio = producto.precio
        else:
            self.__productos[key] = producto

    def buscar_producto(self, nombre: str) -> Optional[Producto]:
        # Retorna el Producto si existe, o None
        if not isinstance(nombre, str):
            return None
        return self.__productos.get(nombre.strip().lower())

    def total_valor_inventario(self) -> float:
        # Suma (precio * stock) de cada producto
        total = 0.0
        for p in self.__productos.values():
            total += p.precio * p.stock
        return total

    def __len__(self) -> int:
        return len(self.__productos)

    def __str__(self) -> str:
        if not self.__productos:
            return "Inventario vacío"
        lineas = ["Inventario:"]
        for p in self.__productos.values():
            lineas.append(str(p))
        lineas.append(f"Total valor: ${self.total_valor_inventario():.2f}")
        return "\n".join(lineas)