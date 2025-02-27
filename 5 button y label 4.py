import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.ventana1.title("Prueba")

        self.boton1 = tk.Button(self.ventana1, text="1",command=self.presion1)
        self.boton1.grid(column=0,row=0)

        self.boton2 = tk.Button(self.ventana1, text="2", command=self.presion2)
        self.boton2.grid(column=0, row=1)

        self.boton3 = tk.Button(self.ventana1, text="3", command=self.presion3)
        self.boton3.grid(column=0, row=2)

        self.boton4 = tk.Button(self.ventana1, text="4", command=self.presion4)
        self.boton4.grid(column=0, row=3)

        self.boton5 = tk.Button(self.ventana1, text="5", command=self.presion5)
        self.boton5.grid(column=0, row=4)

        self.datos = ""
        self.label1 = tk.Label(self.ventana1,text = self.datos)
        self.label1.grid(column =0, row=5)
        self.ventana1.mainloop()
    def presion1(self):
        self.datos=self.datos+"1"
        self.label1.configure(text=self.datos)
    def presion2(self):
        self.datos=self.datos+"2"
        self.label1.configure(text=self.datos)
    def presion3(self):
        self.datos=self.datos+"3"
        self.label1.configure(text=self.datos)
    def presion4(self):
        self.datos=self.datos+"4"
        self.label1.configure(text=self.datos)
    def presion5(self):
        self.datos=self.datos+"5"
        self.label1.configure(text=self.datos)

aplicacion1=Aplicacion()




