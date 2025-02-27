import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.geometry("400x400")
        self.ventana.title("Ejercicio")

        self.etiqueta = tk.Label(self.ventana, text="Sistema de facturación")
        self.etiqueta.pack()

        self.ventana.mainloop()

aplicacion1 = Aplicacion()
