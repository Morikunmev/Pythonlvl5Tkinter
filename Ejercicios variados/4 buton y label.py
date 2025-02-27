import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.resultado = 0
        self.ventana = tk.Tk()
        self.ventana.title("Prueba")

        self.boton1 = tk.Button(self.ventana,text=1,command=self.presionar1)
        self.boton1.grid(column=0,row=0)

        self.boton1 = tk.Button(self.ventana, text=100, command=self.presionar2)
        self.boton1.grid(column=0, row=1)

        self.etiqueta = tk.Label(self.ventana,text=self.resultado)
        self.etiqueta.grid(column=0,row=2)
        self.etiqueta.mainloop()

    def presionar1(self):
        self.resultado+=1
        self.etiqueta.configure(text=self.resultado)
    def presionar2(self):
        self.resultado+=100
        self.etiqueta.configure(text=self.resultado)
aplicacion1 = Aplicacion()

