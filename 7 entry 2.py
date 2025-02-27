import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        self.texto = tk.Label(self.ventana,text="Ingrese nombre de usuario: ")
        self.texto.grid(column=0,row=0)

        self.dato = tk.StringVar()
        self.entrada = tk.Entry(self.ventana,width=20,textvariable=self.dato)
        self.entrada.grid(column=1,row=0)

        self.boton1 = tk.Button(self.ventana,text="Ingresar",command=self.ingresar)
        self.boton1.grid(column=1,row=1)
        self.ventana.mainloop()
    def ingresar(self):
        self.ventana.title(self.dato.get())

aplicacion1 = Aplicacion()





















