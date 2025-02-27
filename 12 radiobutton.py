import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        self.seleccion = tk.IntVar()
        self.seleccion.set(1)
        self.radi1=tk.Radiobutton(self.ventana,text="Rojo",variable=self.seleccion, value=1)
        self.radi1.grid(column=0,row=0)

        self.radi2 =tk.Radiobutton(self.ventana,text="Verde",variable=self.seleccion,value=2)
        self.radi2.grid(column=0,row=1)

        self.radi3 = tk.Radiobutton(self.ventana,text="Azul",variable=self.seleccion,value=3)
        self.radi3.grid(column=0,row=2)

        self.boton1 = tk.Button(self.ventana,text="Cambiar color",command=self.activar)
        self.boton1.grid(column=0,row=3)


        self.ventana.mainloop()
    def activar(self):
        if self.seleccion.get()==1:
            self.ventana.configure(bg="red")
        if self.seleccion.get()==2:
            self.ventana.configure(bg="green")
        if self.seleccion.get() ==3:
            self.ventana.configure(bg="blue")

aplicacion1 = Aplicacion()