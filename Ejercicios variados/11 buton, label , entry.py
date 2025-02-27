import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Prueba")

        self.texto1 = tk.Label(self.ventana,text="Ingrese numero: ")
        self.texto1.grid(column=0,row =0)

        self.dato1 = tk.StringVar()
        self.entrada1 = tk.Entry(self.ventana,width=30,textvariable=self.dato1)
        self.entrada1.grid(column=1,row=0)

        self.boton1 = tk.Button(self.ventana,text="Calcular Cuadrado",command=self.cuadrado)
        self.boton1.grid(column=2,row=0)

        self.resultado1 = tk.Label(self.ventana,text="Resultado")
        self.resultado1.grid(column=3,row=0)

        self.ventana.mainloop()
    def cuadrado(self):
        valor = int(self.dato1.get())
        cuadrado = valor * valor
        self.resultado1.config(text=cuadrado)



aplicacion1 = Aplicacion()