import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.listbox = tk.Listbox(self.ventana)
        self.listbox.grid(column=0,row=0)
        self.listbox.insert(0,"papas")
        self.listbox.insert(1, "manzanas")
        self.listbox.insert(2, "sandia")
        self.listbox.insert(3, "pera")
        self.listbox.insert(4, "melon")
        self.listbox.insert(5, "naranja")

        self.boton1 = ttk.Button(self.ventana,text="Recuperar",command=self.recuperar)
        self.boton1.grid(column=0,row=1)

        self.label1 = ttk.Label(self.ventana,text="Seleccionada")
        self.label1.grid(column=0,row=2)

        self.ventana.mainloop()
    def recuperar(self):
        if len(self.listbox.curselection())!=0:
            self.label1.config(text=self.listbox.get(self.listbox.curselection()[0]))
aplicacion1 = Aplicacion()
