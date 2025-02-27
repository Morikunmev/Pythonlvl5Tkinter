import tkinter as tk
import sys

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        self.texto1 = tk.Label(self.ventana,text="Cuanto es la raiz de 49?")
        self.texto1.grid(column= 0,row=0)

        self.checkbuttons()
        self.botones()
        self.cambiar_estado()
        self.ventana.mainloop()

    def checkbuttons(self):
        self.seleccion1 = tk.IntVar()
        self.check1 = tk.Checkbutton(self.ventana,text="54",variable=self.seleccion1)
        self.check1.grid(column=0,row=1)

        self.seleccion2 = tk.IntVar()
        self.check2 = tk.Checkbutton(self.ventana,text="Nose",variable=self.seleccion2)
        self.check2.grid(column=0,row=2)

        self.seleccion3 = tk.IntVar()
        self.check3 = tk.Checkbutton(self.ventana,text="7",variable=self.seleccion3,command=self.cambiar_estado)
        self.check3.grid(column=0,row=3)

        self.seleccion4 = tk.IntVar()
        self.check4 = tk.Checkbutton(self.ventana,text="Me quiero ir",variable=self.seleccion4)
        self.check4.grid(column=0,row=4)

        self.seleccion5 = tk.IntVar()
        self.check5 = tk.Checkbutton(self.ventana,text="Estas de acuerdo con esto?",
                                     variable=self.seleccion5,command=self.cambiar_estado)
        self.check5.grid(column=0,row=5)
    def botones(self):
        self.boton1 = tk.Button(self.ventana,text="Sep",width=30,state="disabled",command=self.salir)
        self.boton1.grid(column=0,row=6)
    def cambiar_estado(self):
        if self.seleccion5.get() == 1 and self.seleccion3.get()==1:
            self.boton1.configure(state="normal")
        if self.seleccion5.get()==0 or self.seleccion3.get()==0:
            self.boton1.configure(state="disabled")
    def salir(self):
        self.ventana.title("BIEN NNN")
        self.ventana.after(10000,sys.exit(0))



aplicacion1 = Aplicacion()