import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.resizable(False,False)

        self.textos()
        self.entradas()
        self.botones()
        self.resultados()
        self.ventana.mainloop()

    def textos(self):

        self.texto1 = tk.Label(self.ventana,text="Ingrese valor: ")
        self.texto1.grid(column=0,row=0)

        self.texto2 = tk.Label(self.ventana,text="Ingrese valor: ")
        self.texto2.grid(column=0,row=1)
    def entradas(self):
        self.dato1 = tk.StringVar()
        self.entrada1 = tk.Entry(self.ventana, width=30, textvariable=self.dato1)
        self.entrada1.grid(column=1, row=0)

        self.dato2 = tk.StringVar()
        self.entrada2 = tk.Entry(self.ventana,width=30,textvariable=self.dato2)
        self.entrada2.grid(column=1,row=1)
    def botones(self):
        self.boton1 = tk.Button(self.ventana,text="Sumar",command=self.sumar,width=30)
        self.boton1.grid(column=0,row=2)

        self.boton2 = tk.Button(self.ventana,text="Restar",command=self.restar,width=30)
        self.boton2.grid(column=0,row=3)
    def resultados(self):
        self.resultado1 = tk.Label(self.ventana,text="")
        self.resultado1.grid(column=1,row=2)

        self.resultado2 = tk.Label(self.ventana,text="")
        self.resultado2.grid(column=1,row=3)

    def sumar(self):
        suma = int(self.dato1.get()) + int(self.dato2.get())
        self.resultado1.config(text=suma)
    def restar(self):
        resta = int(self.dato1.get()) - int(self.dato2.get())
        self.resultado2.config(text=resta)




aplicacion1 = Aplicacion()
