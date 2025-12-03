#   Programación Funcional - Parte 2
#   Autora: Eunice Ramona Dávila Lugo
# ------------------------------------------------------
# Código imperativo original 
# ------------------------------------------------------
# def procesar_ventas(ventas):
#     """
#     Código imperativo a convertir.
#     
#     Entrada: Lista de diccionarios con ventas
#     Proceso:
#     1. Filtrar ventas mayores a $100
#     2. Aplicar 15% de impuesto
#     3. Calcular el total
#     """
#     resultado = []
#     total = 0
#
#     for venta in ventas:
#         if venta['monto'] > 100:
#             monto_con_impuesto = venta['monto'] * 1.15
#             nueva_venta = {
#                 'id': venta['id'],
#                 'monto_original': venta['monto'],
#                 'monto_final': monto_con_impuesto
#             }
#             resultado.append(nueva_venta)
#             total += monto_con_impuesto
#
#     return resultado, total
#
# # Datos de prueba
# ventas_ejemplo = [
#     {'id': 1, 'monto': 50},
#     {'id': 2, 'monto': 150},
#     {'id': 3, 'monto': 200},
#     {'id': 4, 'monto': 80},
#     {'id': 5, 'monto': 300},
# ]
#
# # Prueba
# if __name__ == "__main__":
#     resultado, total = procesar_ventas(ventas_ejemplo)
#
#     print("Resultado procesado (imperativo):")
#     for r in resultado:
#         print(r)
#
#     print("\nTotal:")
#     print(total)

# ------------------------------------------------------
# Código imperativo convertido 
# ------------------------------------------------------

def es_mayor_100(venta):
    """Devuelve True si el monto es mayor a 100."""
    return venta["monto"] > 100

def aplicar_impuesto(venta):
    """Devuelve una nueva venta con monto_final = monto * 1.15."""
    monto_con_impuesto = venta["monto"] * 1.15
    return {
        "id": venta["id"],
        "monto_original": venta["monto"],
        "monto_final": monto_con_impuesto
    }

def sumar_totales(ventas):
    """Suma los montos finales sin modificar la lista."""
    return sum(v["monto_final"] for v in ventas)

def procesar_ventas(ventas):
    """
    Versión funcional del código imperativo.
    1. Filtra ventas > 100
    2. Aplica impuesto del 15%
    3. Calcula total
    """
    filtradas = list(filter(es_mayor_100, ventas))
    procesadas = list(map(aplicar_impuesto, filtradas))
    total = sumar_totales(procesadas)

    return procesadas, total

ventas_ejemplo = [
    {"id": 1, "monto": 50},
    {"id": 2, "monto": 150},
    {"id": 3, "monto": 200},
    {"id": 4, "monto": 80},
    {"id": 5, "monto": 300},
]

if __name__ == "__main__":
    resultado, total = procesar_ventas(ventas_ejemplo)

    print("Resultado procesado:")
    for r in resultado:
        print(r)

    print("\nTotal:")
    print(total)
