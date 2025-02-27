import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.labelframe1 = ttk.Labelframe(self.ventana,text="Login")
        self.labelframe1.grid(column=0,row=0,padx=5,pady =10)
        self.login()
        self.labelframe2 = ttk.Labelframe(self.ventana,text="Operaciones")
        self.labelframe2.grid(column=0,row=1,padx=5,pady=10)
        self.operaciones()
        self.ventana.mainloop()
    def login(self):
        self.label1 = ttk.Label(self.labelframe1,text="Nombre de Usuario: ")
        self.label1.grid(column=0,row=0,padx=4,pady=4)
        self.entry = ttk.Entry(self.labelframe1)
        self.entry.grid(column=1,row=0,padx=4,pady=4)
        self.label2 = ttk.Label(self.labelframe1,text="Ingrese clave: ")
        self.label2.grid(column=0,row=1,padx=4,pady=4)
        self.entry2 = ttk.Entry(self.labelframe1,show="*")
        self.entry2.grid(column=1,row=1,padx=4,pady=4)
        self.boton1 = ttk.Button(self.labelframe1,text="Ingresar")
        self.boton1.grid(column=1,row=2,padx=4,pady=4)
    def operaciones(self):
        self.boton2 = ttk.Button(self.labelframe2,text="Agregar usuario")
        self.boton2.grid(column=0,row=0,padx=4,pady=4)

        self.boton3 = ttk.Button(self.labelframe2,text="Modificar usuario")
        self.boton3.grid(column=1,row=0,padx=4,pady=4)

        self.boton4 = ttk.Button(self.labelframe2,text="Borrar Usuario")
        self.boton4.grid(column=2,row=0,padx=4,pady=4)
aplicacion1 = Aplicacion()