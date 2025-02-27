import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        self.texto1 = ttk.Label(self.ventana,text="Selecciona un dia de la semana")
        self.texto1.grid(column=0,row=0)

        self.opcion = tk.StringVar()
        semana = ("lunes","martes","miercores","jueves","viernes","sabado","domingo")
        self.combobox1 = ttk.Combobox(self.ventana,width=5,textvariable=self.opcion,
                                      values=semana,state="readonly")
        self.combobox1.current(0)
        self.combobox1.grid(column=0,row=1)

        self.ventana.mainloop()
aplicacion1 =Aplicacion()