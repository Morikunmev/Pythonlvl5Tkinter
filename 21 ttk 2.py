import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        self.texto1 = ttk.Label(self.ventana,text="Ingrese nombre de usuario: ")
        self.texto1.grid(column=0,row=0)

        self.dato1 = tk.StringVar()
        self.entrada1 = ttk.Entry(self.ventana,width=30,textvariable=self.dato1)
        self.entrada1.grid(column=1,row=0)

        self.texto2 = ttk.Label(self.ventana,text="Ingrese clave: ")
        self.texto2.grid(column=0,row=1)

        self.dato2 = tk.StringVar()
        self.entrada2 = ttk.Entry(self.ventana, width=30, textvariable=self.dato2, show="xd")
        self.entrada2.grid(column=1,row=1)

        self.boton1 = ttk.Button(self.ventana,text="INGRESAR",command=self.ingresar,width=30)
        self.boton1.grid(column=1,row=2)

        self.ventana.mainloop()
    def ingresar(self):
        if self.dato1.get() == "Juan" and self.dato2.get() == "1234":
            self.ventana.title("Correcto")
        else:
            self.ventana.title("Incorrecto")

aplicacion1 = Aplicacion()

