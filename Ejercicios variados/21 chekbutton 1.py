import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        self.texto1 = tk.Label(self.ventana,text="Cuanto es la raiz de 49?")
        self.texto1.grid(column=0,row=0)
        self.checkbuttons()
        self.textos()
        self.botones()
        self.ventana.mainloop()

    def checkbuttons(self):
        self.seleccion1 = tk.IntVar()
        self.check1 = tk.Checkbutton(self.ventana,text="7",variable=self.seleccion1)
        self.check1.grid(column=0,row=1)

        self.seleccion2 = tk.IntVar()
        self.check2 = tk.Checkbutton(self.ventana,text="49",variable=self.seleccion2)
        self.check2.grid(column=0,row=2)

        self.seleccion3 = tk.IntVar()
        self.check3 = tk.Checkbutton(self.ventana,text="42",variable=self.seleccion3)
        self.check3.grid(column=0,row=3)
    def botones(self):
        self.boton1 = tk.Button(self.ventana,text="Verificar",command=self.verificar)
        self.boton1.grid(column=0,row=4)

    def textos(self):
        self.resultado = tk.Label(self.ventana,text="Resultado")
        self.resultado.grid(column=0,row=5)
    def verificar(self):
        if self.seleccion1.get() == 1:
            self.resultado.configure(text="Bien")
        if self.seleccion2.get()==1:
            self.resultado.configure(text="Nop")
        if self.seleccion3.get()==1:
            self.resultado.configure(text="Nop")
        if self.seleccion3.get() == 1 and self.seleccion2.get() == 1:
            self.resultado.configure(text="Retirate")

aplicacion1 = Aplicacion()