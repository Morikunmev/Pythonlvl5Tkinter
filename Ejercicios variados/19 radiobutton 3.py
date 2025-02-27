import tkinter as tk
class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        self.seleccion = tk.IntVar()
        self.seleccion.set(1)

        self.radio1 = tk.Radiobutton(self.ventana,text="Rojo",variable=self.seleccion,value=1)
        self.radio1.grid(column=0,row=0)

        self.radio2 = tk.Radiobutton(self.ventana,text="Verde",variable=self.seleccion,value=2)
        self.radio2.grid(column=0,row=1)

        self.radio3 = tk.Radiobutton(self.ventana,text="Azul",variable=self.seleccion,value=3)
        self.radio3.grid(column=0,row=2)

        self.boton1 = tk.Button(self.ventana,text="Cambiar color",command=self.activar)
        self.boton1.grid(column=0,row =3)

        self.ventana.mainloop()

    def activar(self):
        if self.seleccion.get()==1:
            self.ventana.config(bg ="red")
        if self.seleccion.get()==2:
            self.ventana.config(bg="green")
        if self.seleccion.get()==3:
            self.ventana.config(bg="blue")
nose = Aplicacion()