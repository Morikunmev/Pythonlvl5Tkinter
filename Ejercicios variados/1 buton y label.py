import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.valor = 1
        self.ventana1 = tk.Tk()
        self.ventana1.title("Calculadora")

        self.etiqueta = tk.Label(self.ventana1,text=self.valor)
        self.etiqueta.grid(column=0,row=0)
        self.etiqueta.configure(background="red")

        self.boton1 = tk.Button(self.ventana1,text="incrementar",command=self.incrementar)
        self.boton1.grid(column=0,row=1)

        self.boton2 = tk.Button(self.ventana1,text="Decrementar",command=self.decrementar)
        self.boton2.grid(column=0,row=2)
        self.ventana1.mainloop()
    def incrementar(self):
        self.valor = self.valor + 1
        self.etiqueta.config(text=self.valor)
    def decrementar(self):
        self.valor = self.valor - 1
        self.etiqueta.config(text=self.valor)


aplicacion1 = Aplicacion()