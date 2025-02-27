import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        self.listbox1 = tk.Listbox(self.ventana,selectmode=tk.MULTIPLE)
        self.listbox1.grid(column=0,row=0)
        self.listbox1.insert(0,"Uvas")
        self.listbox1.insert(1,"Naranjas")
        self.listbox1.insert(2,"limon")
        self.listbox1.insert(3,"sandia")
        self.listbox1.insert(4,"melon")
        self.listbox1.insert(5,"Durazno")

        self.boton1 = tk.Button(self.ventana,text="Recuperar",command=self.recuperar)
        self.boton1.grid(column=0,row=1)

        self.label1 = tk.Label(self.ventana,text="Seleccionado: ")
        self.label1.grid(column=0,row=2)
        self.ventana.mainloop()
    def recuperar(self):
        if len(self.listbox1.curselection())!=0:
            todos = ""
            for posicion in self.listbox1.curselection():
                todos+=self.listbox1.get(posicion) + "\n"
            self.label1.configure(text=todos)
aplicacion1 = Aplicacion()