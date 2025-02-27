import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()

        self.listbox1 = tk.Listbox(self.ventana,selectmode=tk.MULTIPLE)
        self.listbox1.grid(column=0,row=0)

        self.listbox1.insert(0,"12")
        self.listbox1.insert(1,"122")
        self.listbox1.insert(2,"21")
        self.listbox1.insert(3,"2312")

        self.boton1 = tk.Button(self.ventana,text="RECUPERAR",command=self.recuperar)
        self.boton1.grid(column=0,row=1)

        self.texto1 = tk.Button(self.ventana,text="SELECCIONADO")
        self.texto1.grid(column=0,row=2)

        self.ventana.mainloop()
    def recuperar(self):
        todos = ""
        if len(self.listbox1.curselection())!=0:
            for i in self.listbox1.curselection():
                todos+=self.listbox1.get(i) + "\n"
            self.texto1.configure(text=todos)




        self.ventana.mainloop()
aplicacion1 = Aplicacion()