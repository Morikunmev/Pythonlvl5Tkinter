import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora")

        self.listbox1 = tk.Listbox(self.ventana)
