from tkinter import ttk
import tkinter as tk
class MiVentana(tk.Tk):
    def __init__(self):
        super().__init__()

        self.estilo = ttk.Style()
        self.estilo.configure("Estilo.TButton", background="red")
        self.estilo.configure("Otro.TButton", background="blue")

        self.estilo.configure("Estilo.TFrame", background="lightblue")  # Añadido para cambiar el fondo del Frame

        self.gestorproducto = ttk.Frame(self, style="Estilo.TFrame")  # Se aplica el estilo al Frame
        self.gestorproducto.grid(column=0, row=0, padx=10, pady=10)

        self.BotonAgregarProducto = ttk.Button(self.gestorproducto, text="Agregar Producto", width=30, command=self.AgregarProducto, style="Estilo.TButton")
        self.BotonAgregarProducto.grid(column=0, row=0, padx=5, pady=5)

        self.BotonModificarProducto = ttk.Button(self.gestorproducto, text="Modificar Producto", width=30, command=self.ModificarProducto, style="Otro.TButton")
        self.BotonModificarProducto.grid(column=0, row=1, padx=5, pady=5)

        self.BotonEliminarProducto = ttk.Button(self.gestorproducto, text="Eliminar Producto", width=30, command=self.EliminarProducto, style="Estilo.TButton")
        self.BotonEliminarProducto.grid(column=0, row=2, padx=5, pady=5)

        self.BotonBuscarProducto = ttk.Button(self.gestorproducto, text="Buscar Producto por id", width=30, command=self.BuscarProducto, style="Estilo.TButton")
        self.BotonBuscarProducto.grid(column=0, row=3, padx=5, pady=5)

    def AgregarProducto(self):
        print("Botón Agregar Producto presionado")

    def ModificarProducto(self):
        print("Botón Modificar Producto presionado")

    def EliminarProducto(self):
        print("Botón Eliminar Producto presionado")

    def BuscarProducto(self):
        print("Botón Buscar Producto presionado")

if __name__ == "__main__":
    app = MiVentana()
    app.mainloop()

