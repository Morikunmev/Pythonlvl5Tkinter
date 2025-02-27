import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        self.seleccion = tk.IntVar()
        self.seleccion.set(2)

        self.radio1 = tk.Radiobutton(self.ventana,text="Varon",variable=self.seleccion,value=1)
        self.radio1.grid(column=0,row=0)

        self.radio2 = tk.Radiobutton(self.ventana,text = "Mujer",variable=self.seleccion,value=2)
        self.radio2.grid(column=0,row=1)

        self.boton1 = tk.Button(self.ventana,text="Mostrar seleccionado",command=self.mostrar_seleccionado)
        self.boton1.grid(column=0,row=2)

        self.texto1 = tk.Label(self.ventana,text="Opcion seleccionada: ")
        self.texto1.grid(column=0,row=3)

        self.ventana.mainloop()
    def mostrar_seleccionado(self):
        if self.seleccion.get() == 1:
            self.texto1.configure(text="Opcion seleccionada: varon")
        if self.seleccion.get() == 2:
            self.texto1.configure(text="Opcion seleccionada: mujer")

nose = Aplicacion()