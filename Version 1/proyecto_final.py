#Ejercicio final Curso IBM Python

"""
    #Author: Carlos G. Pascual
    #Date: 07/05/2024

"""

#Creamos unas clases para ejecutar las opciones más adelante
class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

    #De forma predeterminada indicamos las tareas como completadas
    def tarea_completada(self):
        self.completada = True

    #Mostramos el estado de la tarea con un condicional
    def __str__(self) -> str:
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.descripcion} ({estado})" #Le damos formato al texto para que quede de una manera más profesional
    

#Creamos una nueva clase para controlar la lista de tareas

class Listado_Tareas:
    def __init__(self):
        self.tareas = [] #Hemos creado una lista vacia, esta lista se llama tareas

    def nueva_tarea(self, descripcion):
         tarea = Tarea(descripcion)
         self.tareas.append(tarea) #Añadimos la tarea a la lista mediante append y le pasamos los datos por parámetros (tarea)

    #Vamos a indicar si la tarea está completada
    def tarea_completa(self, posicion):
        #Controlamos mediante un try si la tarea no está en la lista
        try:
          tarea = self.tareas[posicion] #Nos moveremos pasando la posición en la lista
          tarea.tarea_completada()
        except IndexError:
          print('Lo siento, no existe esa tarea en la lista.')

    #Mostramos todas las tareas
    def listar_tareas(self):

        #Recorremos la lista mediante un for
        for i, tarea in enumerate(self.tareas):
            print(f"{i}: {tarea}") #Mostramos por consola con el texto formateado

    #Eliminar tareas
    def eliminar_tareas(self, posicion): #le pasaremos la posición que queremos eliminar
        try:
          del self.tareas[posicion]
        except IndexError:
          print("La tarea indicada no existe en la lista")

if __name__ == "__main__":
    lista = Listado_Tareas()

    #Creamos un While para que el programa no se detenga hasta que el usuario elija salir
    while True:

        print("*** Bienvenido al gestor de Tareas ***")

        print("")
        print("Menú de opciones")
        print("1. Agregar Tarea")
        print("2. Ver todas las tareas")
        print("3. Marcar una tarea como completada")
        print("4. Eliminar una Tarea")
        print("5. Salir de la aplicación")

        #Guardamos en una variable la opción elegida
        opcion = input("Por favor introduce el número de opción elegida:")

        if opcion == "1":
            descripcion = input("Introduzca la tarea: ")
            lista.nueva_tarea(descripcion) #Pasamos la descripción por parámetros a la lista
            print("Tarea agregada con exito.")

        elif opcion	== "2":
            lista.listar_tareas() #Mostramos todas las tareas que tenemos

        elif opcion == "3":
            posicion = int(input("¿Que tarea quieres marcar como completada?: "))
            lista.tarea_completa(posicion)

        elif opcion == "4":
            posicion = int(input("Por favor introduce el número de tarea a eliminar: "))
            lista.eliminar_tareas(posicion) #Eliminamos la tarea pasando la posición por parámetros
            print("Tarea eliminada con exito")

        elif opcion == "5":
            consulta = input("¿Estás seguro de que quieres salir (S/N)?: ")
            if consulta.lower() == "s":
                print("Gracias por usar la aplicación, te esperamos pronto...")
                break
            else:
                print("Operación cancelada con exito")

        else:
            print("La opción seleccionada no está disponible, intentalo de nuevo") 