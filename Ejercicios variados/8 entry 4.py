import tkinter as tk

class Aplicacion:

    def __init__(self):
        self.valor1 = 0
        self.valor2 = 0
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora")
        self.ventana.resizable(False,False)

        self.botones()
        self.resultado()

        self.ventana.mainloop()
    def botones(self):
        self.boton1 = tk.Button(self.ventana,text="SUMAR",command=self.sumar)
        self.boton1.grid(column=0,row=0)

        self.boton3 = tk.Button(self.ventana,text = "RESTAR",command=self)

        self.boton2 = tk.Button(self.ventana,text="RESTAR",command=self.restar)
        self.boton2.grid(column=0,row=1)
    def resultado(self):
        self.resultado1 = tk.Label(self.ventana,text= self.valor1)
        self.resultado1.grid(column=1,row=0)

        self.resultado2 = tk.Label(self.ventana,text=self.valor2)
        self.resultado2.grid(column=1,row=1)
    def sumar(self):
        self.valor1+=1
        self.resultado1.config(text=self.valor1)
    def restar(self):
        self.valor2-=1
        self.resultado2.config(text=self.valor2)

aplicacion1 = Aplicacion()
