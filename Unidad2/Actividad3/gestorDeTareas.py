import json

class Tarea:
    def __init__(self, titulo, descripcion, tipo="Normal"):
        self._titulo = titulo
        self._descripcion = descripcion
        self._completada = False
        self._tipo = tipo

    @property
    def titulo(self):
        return self._titulo

    @property
    def descripcion(self):
        return self._descripcion

    @property
    def completada(self):
        return self._completada

    def marcar_completada(self):
        self._completada = True

    def mostrar_info(self):
        estado = "Completada" if self._completada else "Pendiente"
        print(f"[{self._tipo}] {self._titulo} - {estado}\nDescripción: {self._descripcion}")

    def a_diccionario(self):
        return {
            "titulo": self._titulo,
            "descripcion": self._descripcion,
            "completada": self._completada,
            "tipo": self._tipo
        }

class TareaUrgente(Tarea):
    def __init__(self, titulo, descripcion):
        super().__init__(titulo, descripcion, tipo="Urgente")

    def mostrar_info(self):
        estado = "Completada" if self._completada else "Pendiente"
        print(f"[URGENTE] {self._titulo.upper()} - {estado}\nDescripción: {self._descripcion}")

class TareaRecurrente(Tarea):
    def __init__(self, titulo, descripcion):
        super().__init__(titulo, descripcion, tipo="Recurrente")

    def mostrar_info(self):
        estado = "Completada" if self._completada else "Pendiente"
        print(f"[Recurrente] {self._titulo} - {estado}")

class GestorTareas:
    def __init__(self, archivo="tareas.json"):
        self.tareas = []
        self.archivo = archivo
        self.cargar_desde_archivo()

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        print("Tarea agregada")

    def listar_tareas(self):
        if not self.tareas:
            print("No hay tareas registradas")
        else:
            for i, tarea in enumerate(self.tareas, 1):
                print(f"\n{i}. ", end="")
                tarea.mostrar_info()

    def marcar_tarea_completada(self, indice):
        try:
            self.tareas[indice - 1].marcar_completada()
            print("Tarea marcada como completada.")
        except IndexError:
            print("Índice no válido.")

    def eliminar_tarea(self, indice):
        try:
            del self.tareas[indice - 1]
            print("Tarea eliminada.")
        except IndexError:
            print("Índice no válido.")

    def guardar_en_archivo(self):
        datos = [t.a_diccionario() for t in self.tareas]
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
        print("Datos guardados en archivo.")

    def cargar_desde_archivo(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                datos = json.load(f)
                for d in datos:
                    tipo = d.get("tipo", "Normal")
                    if tipo == "Urgente":
                        tarea = TareaUrgente(d["titulo"], d["descripcion"])
                    elif tipo == "Recurrente":
                        tarea = TareaRecurrente(d["titulo"], d["descripcion"])
                    else:
                        tarea = Tarea(d["titulo"], d["descripcion"], tipo)
                    if d["completada"]:
                        tarea.marcar_completada()
                    self.tareas.append(tarea)
        except FileNotFoundError:
            pass

def menu():
    gestor = GestorTareas()

    while True:
        print("\n GESTIÓN DE TAREAS")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Guardar y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            descripcion = input("Descripción: ")
            tipo = input("Tipo (normal/urgente/recurrente): ").lower()

            if tipo == "urgente":
                tarea = TareaUrgente(titulo, descripcion)
            elif tipo == "recurrente":
                tarea = TareaRecurrente(titulo, descripcion)
            else:
                tarea = Tarea(titulo, descripcion)

            gestor.agregar_tarea(tarea)

        elif opcion == "2":
            gestor.listar_tareas()

        elif opcion == "3":
            gestor.listar_tareas()
            indice = int(input("Número de tarea a marcar: "))
            gestor.marcar_tarea_completada(indice)

        elif opcion == "4":
            gestor.listar_tareas()
            indice = int(input("Número de tarea a eliminar: "))
            gestor.eliminar_tarea(indice)

        elif opcion == "5":
            gestor.guardar_en_archivo()
            print("Salir")
            break

        else:
            print("Opción no válida, intenta de nuevo")

if __name__ == "__main__":
    menu()
