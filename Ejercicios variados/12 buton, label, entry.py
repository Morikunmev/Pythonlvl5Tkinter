import tkinter as tk

class Calculadora:
    def __init__(self):
        self.ventana = tk.Tk()

        self.texto1 = tk.Label(self.ventana,text="Calcular cuadrado: ")
        self.texto1.grid(column=0,row=0)
        self.texto2 = tk.Label(self.ventana,text="Calcular potencia: ")
        self.texto2.grid(column=0,row=1)

        self.dato1 = tk.StringVar()
        self.entrada1 = tk.Entry(self.ventana,textvariable=self.dato1,width=30)
        self.entrada1.grid(column=1,row=0)

        self.dato2 = tk.StringVar()
        self.entrada2 = tk.Entry(self.ventana,textvariable=self.dato2,width=30)
        self.entrada2.grid(column=1,row=1)

        self.boton1 = tk.Button(self.ventana,text="CALCULAR",command=self.calcular_cuadrado)
        self.boton1.grid(column=2,row=0)

        self.boton2 = tk.Button(self.ventana,text="CALCULAR",command=self.calcular_potencia)
        self.boton2.grid(column=2,row =1)

        self.resultado1 = tk.Label(self.ventana,text="RESULTADO")
        self.resultado1.grid(column=3,row=0)

        self.resultado2 = tk.Label(self.ventana,text="RESULTADO")
        self.resultado2.grid(column=3,row=1)

        self.ventana.mainloop()
    def calcular_cuadrado(self):
        cuadrado = int(self.dato1.get()) ** 2
        self.resultado1.config(text=cuadrado)
    def calcular_potencia(self):
        potencia = int(self.dato2.get()) ** int(self.dato2.get())
        self.resultado2.config(text=potencia)

calculadora1 = Calculadora()
