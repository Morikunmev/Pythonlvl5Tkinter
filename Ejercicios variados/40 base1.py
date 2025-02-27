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

        ttk.Button(self.tab_eventos, text="Agregar Evento", command=lambda: self.agregar_evento(fecha_entry, hora_entry)).grid(column=1, row=4, padx=10, pady=10, sticky="e")

        tree_columns = ['Nombre del Evento', 'Cantidad de Personas', 'Fecha', 'Hora']
        self.treeview = ttk.Treeview(self.tab_eventos, columns=tree_columns, show='headings')
        for column in tree_columns:
            self.treeview.heading(column, text=column)
        self.treeview.grid(column=0, row=5, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Agregar barras de desplazamiento
        y_scrollbar = ttk.Scrollbar(self.tab_eventos, orient="vertical", command=self.treeview.yview)
        y_scrollbar.grid(row=5, column=2, sticky="ns")
        x_scrollbar = ttk.Scrollbar(self.tab_eventos, orient="horizontal", command=self.treeview.xview)
        x_scrollbar.grid(row=6, column=0, columnspan=2, sticky="ew")

        self.treeview.configure(yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set)

        self.tab_eventos.columnconfigure(0, weight=1)
        self.tab_eventos.rowconfigure(5, weight=1)

    def validar_fecha_hora(self, fecha, hora):
        # Validar el formato de la fecha (YYYY-MM-DD) y la hora (HH:MM:SS)
        formato_fecha_valido = len(fecha) == 10 and fecha[4] == fecha[7] == '-'
        formato_hora_valido = len(hora) == 8 and hora[2] == hora[5] == ':'
        return formato_fecha_valido and formato_hora_valido

    def agregar_evento(self, fecha_entry, hora_entry):
        # Obtener los datos ingresados por el usuario
        nombre_evento = self.tab_eventos.grid_slaves(row=0, column=1)[0].get()
        cantidad_personas = self.tab_eventos.grid_slaves(row=1, column=1)[0].get()
        fecha = fecha_entry.get()
        hora = hora_entry.get()

        # Validar el formato de la fecha y la hora
        if not self.validar_fecha_hora(fecha, hora):
            tk.messagebox.showerror("Error", "Ingrese una fecha y hora válidas (YYYY-MM-DD y HH:MM:SS)")
            return

        # Crear una instancia de la clase Evento con los datos ingresados
        nuevo_evento = Evento(nombre_evento, cantidad_personas, fecha, hora)

        # Agregar el evento a la lista de eventos
        self.eventos.append(nuevo_evento)

        # Actualizar la visualización de la lista de eventos en la interfaz gráfica
        self.treeview.delete(*self.treeview.get_children())
        for evento in self.eventos:
            self.treeview.insert('', 'end', values=(evento.nombre_evento, evento.cantidad_personas, evento.fecha, evento.hora))

# Crear la aplicación y ejecutar el bucle principal
app = Aplicacion()
app.mainloop()
