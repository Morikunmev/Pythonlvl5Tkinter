import tkinter as tk
from tkinter import ttk

class MiVentana:
    def __init__(self, root):
        self.root = root
        self.root.title("Ejemplo Treeview")

        # Crear el Treeview
        self.tree = ttk.Treeview(root)
        self.tree["columns"] = ("Cliente", "Evento", "Producto")

        # Configurar las columnas
        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree.column("Cliente", anchor=tk.W, width=200)
        self.tree.column("Evento", anchor=tk.W, width=200)
        self.tree.column("Producto", anchor=tk.W, width=200)

        # Encabezados
        self.tree.heading("#0", text="", anchor=tk.W)
        self.tree.heading("Cliente", text="Cliente", anchor=tk.W)
        self.tree.heading("Evento", text="Evento", anchor=tk.W)
        self.tree.heading("Producto", text="Producto", anchor=tk.W)

        # Campos de entrada para agregar datos
        self.entry_cliente = tk.Entry(root, width=20)
        self.entry_run = tk.Entry(root, width=20)
        self.entry_empresa = tk.Entry(root, width=20)
        self.entry_comuna = tk.Entry(root, width=20)
        self.entry_contacto = tk.Entry(root, width=20)
        self.entry_email = tk.Entry(root, width=20)
        self.entry_pago = tk.Entry(root, width=20)

        self.entry_evento = tk.Entry(root, width=20)
        self.entry_cantidad = tk.Entry(root, width=20)
        self.entry_fecha = tk.Entry(root, width=20)
        self.entry_hora = tk.Entry(root, width=20)

        self.entry_tipo_producto = tk.Entry(root, width=20)
        self.entry_valor_neto = tk.Entry(root, width=20)

        # Botón para agregar datos
        self.btn_agregar = tk.Button(root, text="Agregar Datos", command=self.agregar_datos)

        # Mostrar los elementos en la ventana
        self.tree.pack()

        self.entry_cliente.pack()
        self.entry_run.pack()
        self.entry_empresa.pack()
        self.entry_comuna.pack()
        self.entry_contacto.pack()
        self.entry_email.pack()
        self.entry_pago.pack()

        self.entry_evento.pack()
        self.entry_cantidad.pack()
        self.entry_fecha.pack()
        self.entry_hora.pack()

        self.entry_tipo_producto.pack()
        self.entry_valor_neto.pack()

        self.btn_agregar.pack()

    def agregar_datos(self):
        # Obtener datos de los campos de entrada
        datos_cliente = (
            self.entry_cliente.get(),
            self.entry_run.get(),
            self.entry_empresa.get(),
            self.entry_comuna.get(),
            self.entry_contacto.get(),
            self.entry_email.get(),
            self.entry_pago.get()
        )

        datos_evento = (
            self.entry_evento.get(),
            int(self.entry_cantidad.get()),
            self.entry_fecha.get(),
            self.entry_hora.get()
        )

        datos_producto = (
            self.entry_tipo_producto.get(),
            float(self.entry_valor_neto.get())
        )

        # Insertar datos en el Treeview
        self.tree.insert("", tk.END, values=(*datos_cliente, "", "", ""))
        self.tree.insert("", tk.END, values=("", *datos_evento, ""))
        self.tree.insert("", tk.END, values=("", "", *datos_producto))

        # Limpiar campos de entrada después de agregar datos
        self.limpiar_campos()

    def limpiar_campos(self):
        self.entry_cliente.delete(0, tk.END)
        self.entry_run.delete(0, tk.END)
        self.entry_empresa.delete(0, tk.END)
        self.entry_comuna.delete(0, tk.END)
        self.entry_contacto.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_pago.delete(0, tk.END)

        self.entry_evento.delete(0, tk.END)
        self.entry_cantidad.delete(0, tk.END)
        self.entry_fecha.delete(0, tk.END)
        self.entry_hora.delete(0, tk.END)

        self.entry_tipo_producto.delete(0, tk.END)
        self.entry_valor_neto.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = MiVentana(root)
    root.mainloop()

