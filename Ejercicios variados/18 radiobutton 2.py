import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        self.textos()
        self.entradas()
        self.radios()
        self.botones()
        self.resultados()

        self.ventana.mainloop()
    def textos(self):
        self.etiqueta1 = tk.Label(self.ventana,text="Ingrese primer valor: ")
        self.etiqueta1.grid(column=0,row=0)

        self.etiqueta2 = tk.Label(self.ventana,text="Ingrese segundo valor: ")
        self.etiqueta2.grid(column=0,row=1)

    def entradas(self):
        self.dato1 = tk.StringVar()
        self.entrada1 = tk.Entry(self.ventana,width=20,textvariable=self.dato1)
        self.entrada1.grid(column=1,row=0)

        self.dato2 = tk.StringVar()
        self.entrada2 = tk.Entry(self.ventana,width=20,textvariable=self.dato2)
        self.entrada2.grid(column=1,row=1)
    def radios(self):
        self.seleccion1 = tk.IntVar()
        self.radio1 = tk.Radiobutton(self.ventana,text="sumar",variable=self.seleccion1,value=1)
        self.radio1.grid(column=1,row=2)

        self.radio2 = tk.Radiobutton(self.ventana,text="restar",variable=self.seleccion1,value=2)
        self.radio2.grid(column=1,row=3)
    def botones(self):
        self.boton1 = tk.Button(self.ventana,text="Operar",command=self.operar)
        self.boton1.grid(column=1,row=4)
    def resultados(self):
        self.resultado1 = tk.Label(self.ventana,text="Resultado")
        self.resultado1.grid(column=1,row=5)

    def operar(self):
        if self.seleccion1.get() == 1:
            suma = int(self.dato1.get()) + int(self.dato2.get())
            self.resultado1.config(text=suma)
        if self.seleccion1.get() == 2:
            resta = int(self.dato1.get()) - int(self.dato2.get())
            self.resultado1.config(text=resta)
aplicacion1 = Aplicacion()