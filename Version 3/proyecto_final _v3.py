import tkinter as tk
from tkinter import messagebox

class Tarea:
    """Clase que representa una tarea."""
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

    def __str__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.descripcion} [{estado}]"


class ListaDeTareas:
    """Clase que representa una lista de tareas."""
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion):
        nueva_tarea = Tarea(descripcion)
        self.tareas.append(nueva_tarea)

    def marcar_completada(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].completada = True
        else:
            raise IndexError("Índice de tarea no válido.")

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            del self.tareas[indice]
        else:
            raise IndexError("Índice de tarea no válido.")

    def mostrar_tareas(self):
        return [str(tarea) for tarea in self.tareas]


class App:
    """Clase que representa la aplicación con interfaz gráfica."""
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")

        self.lista_de_tareas = ListaDeTareas()

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.label = tk.Label(self.frame, text="Descripción de la tarea:")
        self.label.grid(row=0, column=0, padx=5, pady=5)

        self.entry = tk.Entry(self.frame, width=30)
        self.entry.grid(row=0, column=1, padx=5, pady=5)

        self.agregar_btn = tk.Button(self.frame, text="Agregar Tarea", command=self.agregar_tarea)
        self.agregar_btn.grid(row=0, column=2, padx=5, pady=5)

        self.tareas_listbox = tk.Listbox(self.frame, width=50)
        self.tareas_listbox.grid(row=1, column=0, columnspan=3, pady=10)

        self.completar_btn = tk.Button(self.frame, text="Marcar como Completada", command=self.marcar_completada)
        self.completar_btn.grid(row=2, column=0, pady=5)

        self.eliminar_btn = tk.Button(self.frame, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.eliminar_btn.grid(row=2, column=1, pady=5)

        self.mostrar_tareas_btn = tk.Button(self.frame, text="Mostrar Tareas", command=self.mostrar_tareas)
        self.mostrar_tareas_btn.grid(row=2, column=2, pady=5)

    def agregar_tarea(self):
        descripcion = self.entry.get()
        if descripcion:
            self.lista_de_tareas.agregar_tarea(descripcion)
            self.entry.delete(0, tk.END)
            self.mostrar_tareas()
        else:
            messagebox.showwarning("Advertencia", "La descripción de la tarea no puede estar vacía.")

    def marcar_completada(self):
        try:
            indice = self.tareas_listbox.curselection()[0]
            self.lista_de_tareas.marcar_completada(indice)
            self.mostrar_tareas()
        except IndexError:
            messagebox.showerror("Error", "Seleccione una tarea para marcar como completada.")

    def eliminar_tarea(self):
        try:
            indice = self.tareas_listbox.curselection()[0]
            self.lista_de_tareas.eliminar_tarea(indice)
            self.mostrar_tareas()
        except IndexError:
            messagebox.showerror("Error", "Seleccione una tarea para eliminar.")

    def mostrar_tareas(self):
        self.tareas_listbox.delete(0, tk.END)
        for tarea in self.lista_de_tareas.mostrar_tareas():
            self.tareas_listbox.insert(tk.END, tarea)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
