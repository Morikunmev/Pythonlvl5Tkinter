import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.labelframe1 = ttk.Labelframe(self.ventana,text="Suma de numeros")
        self.labelframe1.grid(column=0,row=0,padx=10,pady=10)

        self.ventana.mainloop()
aplicacion1 = Aplicacion()