import tkinter as tk
import math


class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora")

        self.textos()
        self.entradas()
        self.botones()
        self.radios()
        self.resultados()

        self.ventana.mainloop()

    def textos(self):
        self.texto1 = tk.Label(self.ventana,text="Ingrese un numero: ")
        self.texto1.grid(column=0,row=0)

    def entradas(self):
        self.dato1 = tk.StringVar()
        self.entrada1 = tk.Entry(self.ventana,width=30,textvariable=self.dato1)
        self.entrada1.grid(column=1,row=0)
    def botones(self):
        self.boton1 = tk.Button(self.ventana,text="OPERAR",width=25,command=self.operar)
        self.boton1.grid(column=0,row=1)
    def radios(self):
        self.seleccion=tk.IntVar()
        self.seleccion.set(0)
        self.radio1 = tk.Radiobutton(self.ventana,text="Calcular Potencia",variable=self.seleccion,value=1)
        self.radio1.grid(column=2,row=0)

        self.radio2 = tk.Radiobutton(self.ventana,text="Calcular raiz",variable=self.seleccion,value=2)
        self.radio2.grid(column=3,row=0)
    def resultados(self):
        self.resultado = tk.Label(self.ventana,text="Resultado")
        self.resultado.grid(column=1,row=1)
    def operar(self):
        if self.seleccion.get()==1:
            suma = int(self.dato1.get())**int(self.dato1.get())
            self.resultado.config(text=suma)
            self.ventana.title(suma)
            self.ventana.config(bg="blue")
        if self.seleccion.get()==2:
            conversion = int(self.dato1.get())
            raiz = math.sqrt(conversion)
            self.resultado.config(text=raiz)
            self.ventana.title(raiz)
            self.ventana.config(bg="red")

calculadora = Aplicacion()