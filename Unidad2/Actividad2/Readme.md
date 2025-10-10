# Proyecto: Desarrollar una Clase Inventario

## Autora:
#### Eunice Ramona Dávila Lugo

En este trabajo demostre el uso de **encapsulación, getters/setters y abstracción** en Python a través de dos clases principales:  
`Producto` y `Inventario`.

---

##  Objetivo
Implementar encapsulación con atributos privados, getters/setters y métodos especiales para gestionar productos en un inventario.

---

##  Estructura del proyecto
Actividad2/  
├─ producto.py  
├─ inventario.py  
├─ main.py  
└─ Readme.md  

---

##  Diseño de las clases

### Clase `Producto`
Representa un artículo individual dentro del inventario.

**Atributos:**
- `nombre` → Público (`str`)  
- `__stock` → Privado (`int`)  
- `_precio` → Protegido (`float`)

**Métodos:**
- `__init__`: Valida nombre y precio > 0.  
- `@property stock`: Controla acceso al stock (evita valores negativos).  
- `@property precio`: Controla acceso al precio (valida que sea > 0).  
- `__str__`: Muestra los datos legibles.  
- `__eq__`: Compara productos por nombre (sin importar mayúsculas).

---

### Clase `Inventario`
Administra todos los productos mediante un **diccionario privado**.

**Atributos:**
- `__productos`: Diccionario privado (`nombre → Producto`).

**Métodos:**
- `agregar_producto(producto)`: Agrega o actualiza si ya existe (usa setters).  
- `buscar_producto(nombre)`: Devuelve el producto si existe.  
- `total_valor_inventario()`: Calcula el valor total (`precio * stock`).  
- `__len__`: Retorna la cantidad de productos.  
- `__str__`: Muestra todos los productos en formato legible.

---

##  Explicación del diseño

- **Encapsulación:**  
  Use atributos privados (`__stock`) y protegidos (`_precio`) para **ocultar los datos internos** y evitar modificaciones directas.  
  Esto garantiza que los valores pasen por validaciones antes de ser cambiados.

- **Getters y Setters:**  
  Permiten **controlar cómo se leen y modifican los atributos**, aplicando reglas como “el precio no puede ser negativo” o “el stock debe ser entero”.  
  Gracias a esto, pude hacer que el código sea más seguro y mantiene la integridad de los datos.

- **Abstracción:**  
  La clase `Inventario` maneja las operaciones internas (búsqueda, suma, actualización) sin que el usuario tenga que preocuparse por cómo funciona internamente.  
  Solo use métodos claros como `agregar_producto()` o `buscar_producto()`.

---

##  Ejemplo de ejecución

**Archivo:** `main.py`

```python
from producto import Producto
from inventario import Inventario

def main():
    invent = Inventario()

    laptop = Producto("Laptop", 15000.0)
    laptop.stock = 5

    mouse = Producto("Mouse", 250.0)
    mouse.stock = 10

    teclado = Producto("Teclado", 800.0)
    teclado.stock = 7

    audifonos = Producto("Audífonos", 600.0)
    audifonos.stock = 8

    invent.agregar_producto(laptop)
    invent.agregar_producto(mouse)
    invent.agregar_producto(teclado)
    invent.agregar_producto(audifonos)

    print("--- Inventario inicial ---")
    print(invent)

    mouse.precio = 230.0
    mouse.stock = 12
    audifonos.precio = 550.0
    audifonos.stock = 10

    otra_laptop = Producto("Laptop", 14800.0)
    otra_laptop.stock = 2
    invent.agregar_producto(otra_laptop)

    print("\n--- Inventario después de actualizaciones ---")
    print(invent)

    total = invent.total_valor_inventario()
    print(f"\nValor total del inventario: ${total:.2f}")

    buscado = invent.buscar_producto("mouse")
    print("\nProducto buscado:", buscado)

    p1 = Producto("USB", 100.0)
    p2 = Producto("usb", 120.0)
    print("\nComparación p1 == p2:", p1 == p2)

if __name__ == '__main__':
    main()

# Salida esperada
--- Inventario inicial ---
Inventario:
Nombre: Laptop, Precio: $15000.00, Stock: 5
Nombre: Mouse, Precio: $250.00, Stock: 10
Nombre: Teclado, Precio: $800.00, Stock: 7
Nombre: Audífonos, Precio: $600.00, Stock: 8
Total valor: $86900.00

--- Inventario después de actualizaciones ---
Inventario:
Nombre: Laptop, Precio: $14800.00, Stock: 7
Nombre: Mouse, Precio: $230.00, Stock: 12
Nombre: Teclado, Precio: $800.00, Stock: 7
Nombre: Audífonos, Precio: $550.00, Stock: 10
Total valor: $106860.00

Valor total del inventario: $106860.00

Producto buscado: Nombre: Mouse, Precio: $230.00, Stock: 12

Comparación p1 == p2: True