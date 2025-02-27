import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        self.seleccion1 = tk.IntVar()
        self.seleccion1.set(2)

        self.radio1 = ttk.Radiobutton(self.ventana,text="Varon",variable=self.seleccion1,value=1)
        self.radio1.grid(column=0,row=0)

        self.radio2 = ttk.Radiobutton(self.ventana,text="Mujer",variable=self.seleccion1,value=2)
        self.radio2.grid(column=0,row=1)

        self.boton1 = ttk.Button(self.ventana,text="Mostrar seleccionado",command=self.mostrar_seleccionado)
        self.boton1.grid(column=0,row=2)

        self.label1=ttk.Label(self.ventana,text="Opcion seleccionada")
        self.label1.grid(column=0,row=3)

        self.ventana.mainloop()
    def mostrar_seleccionado(self):
        if self.seleccion1.get() == 1:
            self.label1.configure(text="opcion seleccionada: varon")
        if self.seleccion1.get() ==2:
            self.label1.configure(text="opcion seleccionada: mujer")
aplicacion1 = Aplicacion()