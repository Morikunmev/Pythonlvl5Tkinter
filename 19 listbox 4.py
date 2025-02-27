import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.texto1 = tk.Label(self.ventana,text="Ingrese nombre: ")
        self.texto1.grid(column=0,row=0)

        self.texto2 = tk.Label(self.ventana,text="Seleccione pais")
        self.texto2.grid(column=0,row=2)

        self.nombre = tk.StringVar()
        self.entrada1=tk.Entry(self.ventana,width=40,textvariable=self.nombre)
        self.entrada1.grid(column=0,row=1)

        self.listbox = tk.Listbox(self.ventana)
        self.listbox.grid(column=0,row=3)
        self.listbox.insert(0,"Argentina")
        self.listbox.insert(1,"Chile")
        self.listbox.insert(2, "Brasil")
        self.listbox.insert(3, "Peru")
        self.listbox.insert(4, "Mexico")
        self.boton1 = tk.Button(self.ventana,text="Recuperar",command=self.mostrardatos)
        self.boton1.grid(column=0,row=4)
        self.ventana.mainloop()
    def mostrardatos(self):
        if len(self.listbox.curselection())!=0:
            self.ventana.title("Nombre: "+self.nombre.get()+" Pais: "+self.listbox.get(self.listbox.curselection()[0]))
nose = Aplicacion()