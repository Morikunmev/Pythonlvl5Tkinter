import tkinter as tk
from tkinter import ttk
class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.geometry("800x600")
        self.ventana.resizable(0,0)

        self.boton1 = ttk.Button(self.ventana,text="Confirmar")
        self.boton1.place(x=680,y=550,width =90, height = 30)

        self.boton2 = ttk.Button(self.ventana,text="Cancelar")
        self.boton2.place(x=550,y=550,width = 90, height=30)

        self.ventana.mainloop()
aplicacion1 = Aplicacion()