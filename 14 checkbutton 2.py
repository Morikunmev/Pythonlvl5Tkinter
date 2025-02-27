import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        self.seleccion1 = tk.IntVar()
        self.check1 = tk.Checkbutton(self.ventana,text="Esta de acuerdo con los terminos y condiciones?",
                                     variable=self.seleccion1,command=self.cambiar_estado)
        self.check1.grid(column=0,row =0)

        self.boton1 = tk.Button(self.ventana,text="Entrar",state="disabled",command=self.ingresar)
        self.boton1.grid(column=0,row=1)
        self.ventana.mainloop()
    def cambiar_estado(self):
        if self.seleccion1.get()==1:
            self.boton1.config(state="normal")
        if self.seleccion1.get()==0:
            self.boton1.config(state="disabled")
    def ingresar(self):
        self.ventana.title("Ingresando...")
aplicacion1 = Aplicacion()