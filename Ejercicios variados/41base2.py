import tkinter as tk
from tkinter import ttk, messagebox

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

        self.agregar_button = tk.Button(root, text="Agregar Cliente", command=self.agregar_cliente)
        self.agregar_button.pack()

        self.modificar_button = tk.Button(root, text="Modificar Cliente", command=self.modificar_cliente)
        self.modificar_button.pack()

        self.treeview = ttk.Treeview(root, columns=("Nombre", "RUN"))
        self.treeview.heading("#0", text="ID")
        self.treeview.heading("Nombre", text="Nombre")
        self.treeview.heading("RUN", text="RUN")
        self.treeview.pack()

    def actualizar_treeview(self):
        self.treeview.delete(*self.treeview.get_children())
        for idx, (run, nombre) in enumerate(self.clientes.items(), start=1):
            self.treeview.insert("", idx, values=(nombre, run))

    def agregar_cliente(self):
        nombre = self.nombre_entry.get()
        run = self.run_entry.get()

        if nombre and run:
            self.clientes[run] = nombre
            messagebox.showinfo("Éxito", "Cliente agregado correctamente.")
            self.actualizar_treeview()
        else:
            messagebox.showerror("Error", "Por favor, completa todos los campos.")

    def modificar_cliente(self):
        nombre = self.nombre_entry.get()
        run = self.run_entry.get()

        if nombre and run:
            if run in self.clientes:
                self.clientes[run] = nombre
                messagebox.showinfo("Éxito", "Cliente modificado correctamente.")
                self.actualizar_treeview()
            else:
                messagebox.showerror("Error", "Cliente no encontrado.")
        else:
            messagebox.showerror("Error", "Por favor, completa todos los campos.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GestionClientesApp(root)
    root.mainloop()
