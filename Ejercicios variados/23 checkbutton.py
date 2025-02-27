import tkinter as tk
import sys
class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        self.texto1 = tk.Label(self.ventana,text="Selecciona la opcion a guardar")
        self.texto1.grid(column=0,row=0)

        self.radios()
        self.checkbutons()
        self.botones()
        self.ventana.mainloop()
    def radios(self):
        self.seleccion1 = tk.IntVar()
        self.radio1 = tk.Radiobutton(self.ventana,text="TXT",variable=self.seleccion1,value=1,command=self.estado)
        self.radio1.grid(column=0,row=1)

        self.radio2 = tk.Radiobutton(self.ventana,text="PDX",variable=self.seleccion1,value=2,command=self.estado)
        self.radio2.grid(column=1,row=1)
    def checkbutons(self):
        self.seleccion11 = tk.IntVar()
        self.check1 = tk.Checkbutton(self.ventana,text="Acepta los terminos y servicios?",variable=self.seleccion11,command=self.estado)
        self.check1.grid(column=0,row=2)

    def botones(self):
        self.boton1 = tk.Button(self.ventana,text="Sep",state="disabled",command=self.salir)
        self.boton1.grid(column=0,row=3)
    def estado(self):
        if self.seleccion11.get() == 1 and self.seleccion1.get() ==1:
            self.boton1.configure(state="normal")
        if self.seleccion11.get()== 0 and self.seleccion1.get() ==1:
            self.boton1.configure(state="disabled")
    def salir(self):
        sys.exit(0)

aplicacion1 = Aplicacion()











