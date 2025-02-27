import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        self.label1 = tk.Label(self.ventana,text="Ingrese primer valor: ")
        self.label1.grid(column=0,row=0)

        self.dato1 = tk.StringVar()
        self.entrada1 = tk.Entry(self.ventana,width=20,textvariable=self.dato1)
        self.entrada1.grid(column=1,row=0)

        self.label2 = tk.Label(self.ventana,text="Ingrese segundo valor: ")
        self.label2.grid(column=0,row =1)

        self.dato2 = tk.StringVar()
        self.entrada2 = tk.Entry(self.ventana,width=20,textvariable=self.dato2)
        self.entrada2.grid(column=1,row =1)

        self.seleccion = tk.IntVar()
        self.radio1 = tk.Radiobutton(self.ventana,text = "SUMAR",variable=self.seleccion,value=1)
        self.radio1.grid(column=1,row=2)

        self.radio2 = tk.Radiobutton(self.ventana,text = "RESTAR",variable=self.seleccion,value=2)
        self.radio2.grid(column=1,row=3)

        self.boton1 = tk.Button(self.ventana,text="Operar",command = self.operar)
        self.boton1.grid(column=1,row=4)

        self.label3 = tk.Label(self.ventana,text="Resultado")
        self.label3.grid(column=1,row=5)
        self.ventana.mainloop()
    def operar(self):
        if self.seleccion.get() == 1:
            suma = int(self.dato1.get()) + int(self.dato2.get())
            self.label3.configure(text=suma)
        if self.seleccion.get() == 2:
            resta = int(self.dato1.get()) - int(self.dato2.get())
            self.label3.configure(text =resta)

aplicacion1= Aplicacion()