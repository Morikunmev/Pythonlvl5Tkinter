import tkinter as tk
class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Calculo")

        self.texto = tk.Label(self.ventana,text="Ingrese un numero: ")
        self.texto.grid(column=0,row=0)

        self.dato = tk.StringVar()
        self.entrada = tk.Entry(self.ventana,width=10,textvariable=self.dato)
        self.entrada.grid(column = 0,row = 1)

        self.boton = tk.Button(self.ventana,text="Calcular Cuarado",command=self.cuadrado)
        self.boton.grid(column=0,row=2)

        self.texto2 = tk.Label(self.ventana,text="Resultado")
        self.texto2.grid(column=0,row=3)
        self.ventana.mainloop()

    def cuadrado(self):
        valor = int(self.dato.get())
        cuadrado = valor * valor
        self.texto2.config(text=cuadrado)

aplicacion1 = Aplicacion()


























