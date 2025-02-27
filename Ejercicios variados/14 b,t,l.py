import tkinter as tk

class Calculadora:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora")
        self.ventana.resizable(False,False)

        self.variables()
        self.botones()
        self.resultados()
        self.ventana.mainloop()
    def variables(self):
        self.valor1 = 0
        self.valor2 = 0

    def botones(self):
        self.boton1 = tk.Button(self.ventana,text="SUMAR",command=self.sumar)
        self.boton1.grid(column=0,row=0)

        self.boton2 = tk.Button(self.ventana,text="RESTAR",command=self.restar)
        self.boton2.grid(column=1,row=0)

        self.boton3 = tk.Button(self.ventana,text="SUMAR",command=self.sumar1)
        self.boton3.grid(column=0,row=1)

        self.boton4 = tk.Button(self.ventana, text="RESTAR", command=self.restar1)
        self.boton4.grid(column=1,row=1)

    def resultados(self):
        self.resultado1 = tk.Label(self.ventana,text=self.valor1)
        self.resultado1.grid(column=2,row=0)

        self.resultado2 = tk.Label(self.ventana,text=self.valor2)
        self.resultado2.grid(column=2,row=1)

        self.resultado3 = tk.Label(self.ventana,text=0)
        self.resultado3.grid(column=2,row=3)

        self.resultado4 = tk.Label(self.ventana,text=0)
        self.resultado4.grid(column=2,row=4)
    def sumar(self):
        self.valor1+=1
        self.resultado1.config(text=self.valor1)
        self.actualizar_resultado3()
        self.actualizar_resultado4()
    def restar(self):
        self.valor1-=1
        self.resultado1.config(text=self.valor1)
        self.actualizar_resultado3()
        self.actualizar_resultado4()
    def sumar1(self):
        self.valor2+=1
        self.resultado2.config(text=self.valor2)
        self.actualizar_resultado3()
        self.actualizar_resultado4()
    def restar1(self):
        self.valor2-=1
        self.resultado2.config(text=self.valor2)
        self.actualizar_resultado3()
        self.actualizar_resultado4()

    def actualizar_resultado3(self):
        self.resultado3.config(text=self.valor1 + self.valor2)

    def actualizar_resultado4(self):
        self.resultado4.config(text=self.valor1 * self.valor2)

calculadora1 = Calculadora()