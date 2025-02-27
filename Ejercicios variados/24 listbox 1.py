import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        self.listbox1 =tk.Listbox(self.ventana)
        self.listbox1.grid(column=0,row=0)
        self.listbox1.insert(0,"Argentina")
        self.listbox1.insert(1,"Chile")
        self.listbox1.insert(2,"Huatemala")

        self.boton1 = tk.Button(self.ventana,text="RECUPERAR",command=self.recuperar)
        self.boton1.grid(column=0,row=1)

        self.texto1 = tk.Label(self.ventana,text="SELECCIONADO")
        self.texto1.grid(column=0,row=2)
        self.ventana.mainloop()
    def recuperar(self):
        if len(self.listbox1.curselection())!=0:
            self.texto1.configure(text=self.listbox1.get(self.listbox1.curselection()[0]))

aplicacion1 = Aplicacion()