import tkinter as tk

class Calculadora:
    def __init__(self):
        self.ventana = tk.Tk()

        self.valor1 = 0

        self.boton1 = tk.Button(self.ventana,text = "SUMAR",command=self.potencia)
        self.boton1.grid(column=0,row=0)

        self.resultado1 = tk.Label(self.ventana,text=self.valor1)
        self.resultado1.grid(column=1,row=0)

        self.ventana.mainloop()
    def potencia(self):
        self.valor1+=1
        self.resultado1.config(text=self.valor1)

c = Calculadora()