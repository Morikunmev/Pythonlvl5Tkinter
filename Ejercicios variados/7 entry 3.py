import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora")
        self.ventana.resizable(False,False)

        self.textos()
        self.botones()
        self.resultados()
        self.entradas()

        self.ventana.mainloop()

    def textos(self):
        self.texto1 = tk.Label(self.ventana,text = "Ingrese un valor: ")
        self.texto1.grid(column=0,row=0)

        self.texto2 = tk.Label(self.ventana,text = "Ingrese un valor: ")
        self.texto2.grid(column=0,row=1)
    def botones(self):
        self.boton1 = tk.Button(self.ventana,text="SUMAR: ",width=30,command=self.sumar)
        self.boton1.grid(column=0,row=2)

        self.boton2 = tk.Button(self.ventana,text= "RESTAR: ",width=30,command=self.restar)
        self.boton2.grid(column=0,row=3)

        self.boton3 = tk.Button(self.ventana,text="PRODUCTO: ",width=30,command=self.multiplicar)
        self.boton3.grid(column=0,row=4)

        self.boton4 = tk.Button(self.ventana,text = "DIVIDIR: ",width=30,command=self.dividir)
        self.boton4.grid(column=0,row=5)

    def entradas(self):
        self.dato1 = tk.StringVar()
        self.entrada1 = tk.Entry(self.ventana,width=30,textvariable=self.dato1)
        self.entrada1.grid(column=1,row=0)

        self.dato2 = tk.StringVar()
        self.entrada2 = tk.Entry(self.ventana,width=30,textvariable=self.dato2)
        self.entrada2.grid(column=1,row=1)
    def resultados(self):
        self.resultado1 = tk.Label(self.ventana,text = "Resultado")
        self.resultado1.grid(column=1,row=2)

        self.resultado2 = tk.Label(self.ventana,text = "Resultado")
        self.resultado2.grid(column=1,row=3)

        self.resultado3 = tk.Label(self.ventana,text = "Resultado")
        self.resultado3.grid(column=1,row=4)

        self.resultado4 = tk.Label(self.ventana,text = "Resultado")
        self.resultado4.grid(column=1,row=5)

    def sumar(self):
        suma = int(self.dato1.get()) + int(self.dato2.get())
        self.resultado1.config(text=suma)
    def restar(self):
        resta = int(self.dato1.get()) - int(self.dato2.get())
        self.resultado2.config(text=resta)
    def multiplicar(self):
        mul = int(self.dato1.get()) * int(self.dato2.get())
        self.resultado3.config(text=mul)
    def dividir(self):
        div = int(self.dato1.get()) / int(self.dato2.get())
        div = round(div,2)
        self.resultado4.config(text=div)





aplicacion1= Aplicacion()