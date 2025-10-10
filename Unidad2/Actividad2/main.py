from producto import Producto
from inventario import Inventario

def main():
    invent = Inventario()

    # Crear productos
    laptop = Producto("Laptop", 15000.0)
    laptop.stock = 5

    mouse = Producto("Mouse", 250.0)
    mouse.stock = 10

    teclado = Producto("Teclado", 800.0)
    teclado.stock = 7

    audifonos = Producto("Audífonos", 600.0)
    audifonos.stock = 8

    # productos
    invent.agregar_producto(laptop)
    invent.agregar_producto(mouse)
    invent.agregar_producto(teclado)
    invent.agregar_producto(audifonos)

    print("-------- Inventario inicial --------")
    print(invent)

    # Modificar valores usando setters
    mouse.precio = 230.0
    mouse.stock = 12

    audifonos.precio = 550.0
    audifonos.stock = 10

    otra_laptop = Producto("Laptop", 14800.0)
    otra_laptop.stock = 2
    invent.agregar_producto(otra_laptop)

    print("\n-------- Inventario después de actualizaciones --------")
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