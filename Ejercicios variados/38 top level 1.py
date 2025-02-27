import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()

        self.texto1 = ttk.Label(self.ventana1, text="Ingrese nombre de usuario: ")
        self.texto1.grid(column=0, row=0)

        self.dato1 = tk.StringVar()
        self.entrada1 = tk.Entry(self.ventana1, textvariable=self.dato1, width=30)
        self.entrada1.grid(column=1, row=0)

        self.boton1 = ttk.Button(self.ventana1, text="INGRESAR", command=self.abrir_nueva_ventana)
        self.boton1.grid(column=2, row=0)

        self.ventana1.mainloop()

    def abrir_nueva_ventana(self):
        nueva_ventana = tk.Toplevel(self.ventana1)
        nueva_ventana.title("Nueva Ventana")
        etiqueta_nueva_ventana = ttk.Label(nueva_ventana, text=f"Bienvenido, {self.dato1.get()}, seleccione una opcion: ")
        etiqueta_nueva_ventana.grid(column=0, row=0)

        opcion1 = tk.StringVar()
        opciones = ("Ver informe","Agregar Cliente")
        combobox = ttk.Combobox(nueva_ventana, width=30, textvariable=opcion1, values=opciones, state="readonly")
        combobox.current(0)
        combobox.grid(column=0, row=1)

        boton1 = ttk.Button(nueva_ventana, text="Seleccionar", width=32, command=lambda: self.seleccionar_opcion(combobox.get()))
        boton1.grid(column=0, row=2)

    def seleccionar_opcion(self, opcion):
        if opcion == "Ver informe":
            informe_ventana = tk.Toplevel(self.ventana1)
            informe_ventana.title("Informe")
            etiqueta_informe = ttk.Label(informe_ventana, text="Aquí va el contenido del informe.")
            etiqueta_informe.grid(column=0, row=0)
        elif opcion == "Agregar Cliente":
            cliente_ventana = tk.Toplevel(self.ventana1)
            cliente_ventana.title("Agregar Cliente")
            etiqueta_cliente = ttk.Label(cliente_ventana, text="Formulario para agregar un cliente.")
            etiqueta_cliente.grid(column=0, row=0)

aplicacion1 = Aplicacion()
