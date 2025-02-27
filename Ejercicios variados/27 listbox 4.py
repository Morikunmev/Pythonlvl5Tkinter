import tkinter as tk

class Calculadora:
    def __init__(self):
        self.ventana = tk.Tk()
        self.lisbox1 = tk.Listbox(self.ventana)
        self.lisbox1.grid(column=0,row=0)

        self.lisbox1.insert(0,"Paras")
        self.lisbox1.insert(1,"Manzanas")
        self.lisbox1.insert(2,"melon")
        self.lisbox1.insert(3,"Naranjas")
        self.lisbox1.insert(4,"Cervezas")

        self.boton1 = tk.Button(self.ventana,text="Recuperar",command=self.recuperar)
        self.boton1.grid(column=0,row=1)

        self.resultado = tk.Label(self.ventana,text="Resultado")
        self.resultado.grid(column=0,row=2)

        self.ventana.mainloop()
    def recuperar(self):
        seleccion = self.lisbox1.get(tk.ACTIVE)
        self.resultado.configure(text=seleccion)

calculadora1 = Calculadora()