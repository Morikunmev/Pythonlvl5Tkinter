import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog

class Evento:
    def __init__(self, nombre_evento, cantidad_personas, fecha, hora):
        self.nombre_evento = nombre_evento
        self.cantidad_personas = cantidad_personas
        self.fecha = fecha
        self.hora = hora

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()

        self.eventos = []

        self.title("Gestor de Eventos")
        self.geometry("800x400")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.tab_control = ttk.Notebook(self)
        self.tab_eventos = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_eventos, text='Eventos')
        self.tab_control.grid(column=0, row=0, sticky="nsew")

        self.crear_interfaz_eventos()

    def crear_interfaz_eventos(self):
        # Crear widgets para la pestaña de Eventos
        ttk.Label(self.tab_eventos, text="Nombre del Evento:").grid(column=0, row=0, padx=10, pady=5, sticky="e")
        ttk.Entry(self.tab_eventos, textvariable=tk.StringVar()).grid(column=1, row=0, padx=10, pady=5)

        ttk.Label(self.tab_eventos, text="Cantidad de Personas:").grid(column=0, row=1, padx=10, pady=5, sticky="e")
        ttk.Entry(self.tab_eventos, textvariable=tk.StringVar()).grid(column=1, row=1, padx=10, pady=5)

        ttk.Label(self.tab_eventos, text="Fecha (YYYY-MM-DD):").grid(column=0, row=2, padx=10, pady=5, sticky="e")
        fecha_entry = ttk.Entry(self.tab_eventos, textvariable=tk.StringVar())
        fecha_entry.grid(column=1, row=2, padx=10, pady=5)

        ttk.Label(self.tab_eventos, text="Hora (HH:MM:SS):").grid(column=0, row=3, padx=10, pady=5, sticky="e")
        hora_entry = ttk.Entry(self.tab_eventos, textvariable=tk.StringVar())
        hora_entry.grid(column=1, row=3, padx=10, pady=5)

        ttk.Button(self.tab_eventos, text="Agregar Evento")

        tree_columns = ['Nombre del Evento', 'Cantidad de Personas', 'Fecha', 'Hora']
        self.treeview = ttk.Treeview(self.tab_eventos, columns=tree_columns, show='headings')
        for column in tree_columns:
            self.treeview.heading(column, text=column)
        self.treeview.grid(column=0, row=5, columnspan=2, padx=10, pady=10, sticky="nsew")
aplicacion1 = Aplicacion()