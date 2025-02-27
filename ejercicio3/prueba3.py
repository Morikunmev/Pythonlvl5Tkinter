import tkinter as tk
import sys

class Ventana_Principal:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Empresa New food: Inicio Sesion")
        self.ventana.geometry("400x400")
        self.ventana.resizable(False,False)

        self.ventana.mainloop()


aplicacion1 = Ventana_Principal()
