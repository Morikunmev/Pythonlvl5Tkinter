import tkinter as tk


class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Prueba del control entry")

        self.etiqueta = tk.Label(self.ventana,text="Ingrese un numero: ")
        self.etiqueta.grid(column =0,row = 0)

        self.dato = tk.StringVar()
        self.entry = tk.Entry(self.ventana,width=10,textvariable=self.dato)
        self.entry.grid(column = 0,row = 1)

        self.boton = tk.Button(self.ventana,text="Calcular Cuadrado",command=self.calcularcuadrado)
        self.boton.grid(column=0,row=2)

        self.etiqueta2 = tk.Label(self.ventana,text="Resultado")
        self.etiqueta2.grid(column=0,row=3)
        self.ventana.mainloop()
    def calcularcuadrado(self):
        valor = int(self.dato.get())
        cuadrado = valor * valor
        self.etiqueta2.config(text=cuadrado)
aplicacion1 = Aplicacion()