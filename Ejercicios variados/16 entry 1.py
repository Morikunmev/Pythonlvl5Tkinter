import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        self.texto1 = tk.Label(self.ventana,text="Ingrese un numero: ")
        self.texto1.grid(column=0,row=0)

        self.texto2 = tk.Label(self.ventana,text="Ingrese un numero: ")
        self.texto2.grid(column=0,row=1)

        self.dato1 = tk.StringVar()
        self.entrada1 = tk.Entry(self.ventana,width=10,textvariable=self.dato1)
        self.entrada1.grid(column=1,row=0)

        self.dato2 = tk.StringVar()
        self.entrada2 = tk.Entry(self.ventana,width=10,textvariable=self.dato2)
        self.entrada2.grid(column=1,row =1)

        self.boton1 = tk.Button(self.ventana,text="Calcular Suma",command=self.sumar)
        self.boton1.grid(column=0,row=2)

        self.resultado1 = tk.Label(self.ventana,text="Resultado")
        self.resultado1.grid(column=1,row=2)

        self.ventana.mainloop()
    def sumar(self):
        suma = int(self.dato1.get()) + int(self.dato2.get())
        self.resultado1.config(text=suma)

aplicacion1 = Aplicacion()