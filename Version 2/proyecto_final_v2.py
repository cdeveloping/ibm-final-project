import json

#usaremos un archivo Json para guardar y volver a cargar los datos

import json

class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

    def marcar_como_completada(self):
        self.completada = True

    def __str__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.descripcion} - {estado}"

class ListaDeTareas:
    def __init__(self):
        self.tareas = []
        self.cargar_tareas()

    def agregar_tarea(self, descripcion):
        nueva_tarea = Tarea(descripcion)
        self.tareas.append(nueva_tarea)
        self.guardar_tareas()

    def marcar_tarea_como_completada(self, indice):
        try:
            self.tareas[indice].marcar_como_completada()
            self.guardar_tareas()
        except IndexError:
            print("Error: No existe una tarea con ese índice.")

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas pendientes.")
        else:
            for i, tarea in enumerate(self.tareas):
                print(f"{i + 1}. {tarea}")

    def eliminar_tarea(self, indice):
        try:
            self.tareas.pop(indice)
            self.guardar_tareas()
        except IndexError:
            print("Error: No existe una tarea con ese índice.")

    def guardar_tareas(self):
        with open("tareas.json", "w") as archivo:
            tareas_serializadas = [tarea.__dict__ for tarea in self.tareas]
            json.dump(tareas_serializadas, archivo)

    def cargar_tareas(self):
        try:
            with open("tareas.json", "r") as archivo:
                tareas_serializadas = json.load(archivo)
                self.tareas = [Tarea(**datos) for datos in tareas_serializadas]
        except FileNotFoundError:
            self.tareas = []

def menu():
    lista_de_tareas = ListaDeTareas()
    while True:
        print("\n1. Agregar una nueva tarea")
        print("2. Marcar una tarea como completada")
        print("3. Mostrar todas las tareas")
        print("4. Eliminar una tarea")
        print("5. Salir")
        
        try:
            opcion = int(input("Elige una opción: "))
            if opcion == 1:
                descripcion = input("Descripción de la nueva tarea: ")
                lista_de_tareas.agregar_tarea(descripcion)
            elif opcion == 2:
                indice = int(input("Número de la tarea a marcar como completada: ")) - 1
                lista_de_tareas.marcar_tarea_como_completada(indice)
            elif opcion == 3:
                lista_de_tareas.mostrar_tareas()
            elif opcion == 4:
                indice = int(input("Número de la tarea a eliminar: ")) - 1
                lista_de_tareas.eliminar_tarea(indice)
            elif opcion == 5:
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")

if __name__ == "__main__":
    menu()


