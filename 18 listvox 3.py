import tkinter
import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.scrollbar1 = tkinter.Scrollbar(self.ventana,orient=tk.VERTICAL)
        self.listbox1 = tk.Listbox(self.ventana,selectmode=tk.MULTIPLE,yscrollcommand=self.scrollbar1.set)
        self.listbox1.grid(column=0,row=0)
        self.scrollbar1.configure(command=self.listbox1.yview)
        self.scrollbar1.grid(column=1,row=0,sticky="NS")
        self.listbox1.insert(0,"papa")
        self.listbox1.insert(1, "melon")
        self.listbox1.insert(2, "uva")
        self.listbox1.insert(3, "limon")
        self.listbox1.insert(4, "papaya")
        self.listbox1.insert(5,"papa")
        self.listbox1.insert(6, "melon")
        self.listbox1.insert(7, "uva")
        self.listbox1.insert(8, "limon")
        self.listbox1.insert(9, "papaya")
        self.listbox1.insert(10,"papa")
        self.listbox1.insert(11, "melon")
        self.listbox1.insert(12, "uva")
        self.listbox1.insert(13, "limon")
        self.listbox1.insert(14, "papaya")

        self.boton1 = tk.Button(self.ventana,text="Recuperar",command=self.recuperar)
        self.boton1.grid(column=0,row=1)

        self.label1 = tk.Label(self.ventana,text="Seleccionado")
        self.label1.grid(column=0,row=2)
        self.ventana.mainloop()
    def recuperar(self):
        if len(self.listbox1.curselection())!=0:
            todos = ""
            for posicion in self.listbox1.curselection():
                todos+=self.listbox1.get(posicion)+"\n"
            self.label1.configure(text=todos)
aplicacion1 = Aplicacion()