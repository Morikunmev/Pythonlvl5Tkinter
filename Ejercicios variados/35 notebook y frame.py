import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Prueba de control")

        self.cuaderno1 = ttk.Notebook(self.ventana)

        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1,text="Button")
        self.label1 = ttk.Label(self.ventana,text="La clase button nossss")
        self.label1.grid(column=0,row=0)

        self.boton1 = ttk.Button(self.pagina1,text="Ejemplo de boton")
        self.boton1.grid(column=0,row=1)
        self.boton2 = ttk.Button(self.pagina1,text="Ejemplo de boton inactivo",state="disabled")
        self.boton2.grid(column=0,row=2)

        self.pagina2=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2,text="Label")
        self.label2 = ttk.Label(self.pagina2,text="La clase label permite mostrar un mensaje")
        self.label2.grid(column=0,row=0)

        self.label3 = ttk.Label(self.pagina2,text="Xd")
        self.label3.grid(column=0,row=1)

        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3,text="Entry")
        self.label4 = ttk.Label(self.pagina3,text="En tkinter el control de entrada de datos por teclados se llama entry")
        self.label4.grid(column=0,row=0)

        self.entry = ttk.Entry(self.pagina3,width=30)
        self.entry.grid(column=0,row=1)

        self.cuaderno1.grid(column=0,row=0)
        self.ventana.mainloop()
aplicacion1 = Aplicacion()