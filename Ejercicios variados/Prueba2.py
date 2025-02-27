import tkinter as tk
from tkinter import ttk

def llenar_treeview(tree):
    # Insertar elementos en el Treeview
    tree.insert("", "0", "item1", text="Elemento 1")
    tree.insert("item1", "end", text="Subelemento 1.1")
    tree.insert("", "1", "item2", text="Elemento 2")
    tree.insert("item2", "end", text="Subelemento 2.1")

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de Treeview")

# Crear un Treeview
tree = ttk.Treeview(root)
tree.pack(expand=True, fill="both")

# Configurar las columnas
tree["columns"] = ("columna1", "columna2")
tree.column("#0", width=100, minwidth=100)
tree.column("columna1", anchor=tk.W, width=100)
tree.column("columna2", anchor=tk.W, width=100)

# Configurar las cabeceras de las columnas
tree.heading("#0", text="Nombre", anchor=tk.W)
tree.heading("columna1", text="Columna 1", anchor=tk.W)
tree.heading("columna2", text="Columna 2", anchor=tk.W)

# Llenar el Treeview con datos de ejemplo
llenar_treeview(tree)

# Iniciar el bucle principal
root.mainloop()
