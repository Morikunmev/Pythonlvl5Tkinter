import tkinter as tk
from tkinter import ttk

class Cliente:
    def __init__(self, nombre_completo, run, empresa, comuna, numero_contacto, email, metodo_pago):
        self.nombre_completo = nombre_completo
        self.run = run
        self.empresa = empresa
        self.comuna = comuna
        self.numero_contacto = numero_contacto
        self.email = email
        self.metodo_pago = metodo_pago

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()

        self.clientes = []

        self.title("Gestor de Datos")
        self.geometry("800x400")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.tab_control = ttk.Notebook(self)
        self.tab_clientes = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_clientes, text='Clientes')
        self.tab_control.grid(column=0, row=0, sticky="nsew")

        self.crear_interfaz_clientes()

    def crear_interfaz_clientes(self):
        # Crear widgets para la pestaña de Clientes
        ttk.Label(self.tab_clientes, text="Nombre Completo:").grid(column=0, row=0, padx=10, pady=5, sticky="e")
        ttk.Entry(self.tab_clientes, textvariable=tk.StringVar()).grid(column=1, row=0, padx=10, pady=5)

        ttk.Label(self.tab_clientes, text="RUN:").grid(column=0, row=1, padx=10, pady=5, sticky="e")
        ttk.Entry(self.tab_clientes, textvariable=tk.StringVar()).grid(column=1, row=1, padx=10, pady=5)

        ttk.Label(self.tab_clientes, text="Empresa:").grid(column=0, row=2, padx=10, pady=5, sticky="e")
        ttk.Entry(self.tab_clientes, textvariable=tk.StringVar()).grid(column=1, row=2, padx=10, pady=5)

        ttk.Label(self.tab_clientes, text="Comuna:").grid(column=0, row=3, padx=10, pady=5, sticky="e")
        ttk.Entry(self.tab_clientes, textvariable=tk.StringVar()).grid(column=1, row=3, padx=10, pady=5)

        ttk.Label(self.tab_clientes, text="Número de Contacto:").grid(column=0, row=4, padx=10, pady=5, sticky="e")
        ttk.Entry(self.tab_clientes, textvariable=tk.StringVar()).grid(column=1, row=4, padx=10, pady=5)

        ttk.Label(self.tab_clientes, text="Email:").grid(column=0, row=5, padx=10, pady=5, sticky="e")
        ttk.Entry(self.tab_clientes, textvariable=tk.StringVar()).grid(column=1, row=5, padx=10, pady=5)

        ttk.Label(self.tab_clientes, text="Método de Pago:").grid(column=0, row=6, padx=10, pady=5, sticky="e")
        ttk.Entry(self.tab_clientes, textvariable=tk.StringVar()).grid(column=1, row=6, padx=10, pady=5)

        ttk.Button(self.tab_clientes, text="Agregar Cliente")

        tree_columns = ['Nombre Completo', 'RUN', 'Empresa', 'Comuna', 'Número de Contacto', 'Email', 'Método de Pago']
        self.treeview = ttk.Treeview(self.tab_clientes, columns=tree_columns, show='headings')
        for column in tree_columns:
            self.treeview.heading(column, text=column)
        self.treeview.grid(column=0, row=8, columnspan=2, padx=10, pady=10, sticky="nsew")
aplicacion1 = Aplicacion()