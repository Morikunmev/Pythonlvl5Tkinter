import tkinter as tk
from tkinter import messagebox

class GestionClientesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Clientes")

        self.clientes = {}

        self.nombre_label = tk.Label(root, text="Nombre Completo:")
        self.nombre_label.pack()

        self.nombre_entry = tk.Entry(root)
        self.nombre_entry.pack()

        self.run_label = tk.Label(root, text="RUN:")
        self.run_label.pack()

        self.run_entry = tk.Entry(root)
        self.run_entry.pack()

        self.info_label = tk.Label(root, text="")
        self.info_label.pack()

        self.agregar_button = tk.Button(root, text="Agregar Cliente", command=self.agregar_cliente)
        self.agregar_button.pack()

        self.modificar_button = tk.Button(root, text="Modificar Cliente", command=self.modificar_cliente)
        self.modificar_button.pack()

    def actualizar_info_label(self):
        nombre = self.nombre_entry.get()
        run = self.run_entry.get()
        info_text = f"Nombre: {nombre}, RUN: {run}"
        self.info_label.config(text=info_text)

    def agregar_cliente(self):
        nombre = self.nombre_entry.get()
        run = self.run_entry.get()

        if nombre and run:
            self.clientes[run] = nombre
            messagebox.showinfo("Éxito", "Cliente agregado correctamente.")
            self.actualizar_info_label()
        else:
            messagebox.showerror("Error", "Por favor, completa todos los campos.")

    def modificar_cliente(self):
        nombre = self.nombre_entry.get()
        run = self.run_entry.get()

        if nombre and run:
            if run in self.clientes:
                self.clientes[run] = nombre
                messagebox.showinfo("Éxito", "Cliente modificado correctamente.")
                self.actualizar_info_label()
            else:
                messagebox.showerror("Error", "Cliente no encontrado.")
        else:
            messagebox.showerror("Error", "Por favor, completa todos los campos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GestionClientesApp(root)
    root.mainloop()

