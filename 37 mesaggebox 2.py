import tkinter as tk
from tkinter import messagebox as mb
import sys
class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.agregar_menu()
        self.ventana1.mainloop()
    def agregar_menu(self):
        self.menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=self.menubar1)
        self.opciones1 = tk.Menu(self.menubar1)
        self.opciones1.add_command(label="Salir",command=self.salir)
        self.menubar1.add_cascade(label="Opciones",menu=self.opciones1)
    def salir(self):
        respuesta = mb.askyesno("Cuidado","Quieres salir del programa?")
        if respuesta == True:
            sys.exit(0)
aplicacion1 = Aplicacion()