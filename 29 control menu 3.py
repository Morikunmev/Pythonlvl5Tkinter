import tkinter as tk
from tkinter import ttk
import sys
class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        menubar1 = tk.Menu(self.ventana)
        self.ventana.config(menu = menubar1)

        opciones1 = tk.Menu(menubar1)
        opciones1.add_command(label="Cambiar dimension de ventana",command=self.fijartamaño)
        opciones1.add_command(label="Finalizar programa",command=self.finalizar)
        menubar1.add_cascade(label="Opciones",menu=opciones1)

        self.label1 = ttk.Label(self.ventana,text="Ingrese el ancho de la ventana")
        self.label1.grid(column=0,row=0)

        self.dato1 = tk.StringVar()
        self.entrada1 = ttk.Entry(self.ventana,width=10,textvariable=self.dato1)
        self.entrada1.grid(column=0,row=1)

        self.label2 = ttk.Label(self.ventana,text="Ingrese el alto de la ventana")
        self.label2.grid(column=0,row=2)

        self.dato2 = tk.StringVar()
        self.entrada2 = ttk.Entry(self.ventana,width=10,textvariable=self.dato2)
        self.entrada2.grid(column=0,row=3)

        self.ventana.mainloop()
    def fijartamaño(self):
        self.ventana.geometry(self.dato1.get() + "x" +self.dato2.get())
    def finalizar(self):
        sys.exit(0)
aplicacion1 = Aplicacion()
