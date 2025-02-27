import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.labelframe1 = ttk.Labelframe(self.ventana,text="Login")
        self.labelframe1.grid(column=0,row=0,padx=5,pady =10)

        self.labelframe2 = ttk.Labelframe(self.ventana,text="Operaciones")
        self.labelframe2.grid(column=0,row=1,padx=5,pady=10)

        #texto, entrada para labelframe1
        self.label1 = ttk.Label(self.labelframe1,text="Nombre de Usuario: ")
        self.label1.grid(column=0,row=0,padx=4, pady=4)



        self.ventana.mainloop()

operacion1 = Aplicacion()
