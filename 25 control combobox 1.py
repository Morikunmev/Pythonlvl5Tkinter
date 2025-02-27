import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        self.label1 = ttk.Label(self.ventana,text="Seleccione un dia de la semana")
        self.label1.grid(column=0,row=0)

        self.opcion = tk.StringVar()
        diassemana = ("lunes","martes","miercoles","jueves","viernes","sabado","domingo")
        self.combobox1 = ttk.Combobox(self.ventana,width=10,textvariable=self.opcion,
                                      values=diassemana,state="readonly")
        self.combobox1.current(0)
        self.combobox1.grid(column=0,row=1)
        self.boton1 = ttk.Button(self.ventana,text="Recupear",command=self.recuperar)
        self.boton1.grid(column=0,row=2)
        self.label2=ttk.Label(self.ventana,text="Dias seleccionado: ")
        self.label2.grid(column=0,row=3)

        self.ventana.mainloop()
    def recuperar(self):
        self.label2.config(text=self.opcion.get())
aplicacion1 = Aplicacion()