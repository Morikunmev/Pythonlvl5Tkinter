import tkinter as tk

class Calculadora:
    def __init__(self):
        self.ventana = tk.Tk()
        self.lisbox1 = tk.Listbox(self.ventana)
        self.lisbox1.grid(column=0,row=0)

        self.lisbox1.insert(0,"2+2")
        self.lisbox1.insert(1, "2-2")
        self.lisbox1.insert(2, "2*2")
        self.lisbox1.insert(3, "2/2")
        self.lisbox1.insert(4, "2+4")
        self.lisbox1.insert(5, "1+2")

        self.boton1 = tk.Button(self.ventana,text="CALCULAR",command=self.operar)
        self.boton1.grid(column=0,row=1)

        self.texto1 = tk.Label(self.ventana,text="RESULTADO")
        self.texto1.grid(column=0,row=2)

        self.ventana.mainloop()
    def operar(self):
        for i in self.lisbox1.curselection():
            expresion = self.lisbox1.get(i)
            resultado = eval(expresion)
            self.texto1.configure(text=resultado)



        self.ventana.mainloop()

calculadora1 = Calculadora()
