import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.seleccion1 = tk.IntVar()
        self.check1 = tk.Checkbutton(self.ventana,text="Chrome",variable=self.seleccion1,command=self.cambiartitulo)
        self.check1.grid(column=0,row=0)

        self.seleccion2 = tk.IntVar()
        self.check2 = tk.Checkbutton(self.ventana,text="Firefox",variable=self.seleccion2,command=self.cambiartitulo)
        self.check2.grid(column=1,row=0)

        self.seleccion3 = tk.IntVar()
        self.check3 = tk.Checkbutton(self.ventana,text="Edge",variable=self.seleccion3,command=self.cambiartitulo)
        self.check3.grid(column=2,row=0)

        self.seleccion4 = tk.IntVar()
        self.check4 = tk.Checkbutton(self.ventana,text="Opera",variable=self.seleccion4,command=self.cambiartitulo)
        self.check4.grid(column=3,row=0)

        self.ventana.mainloop()

    def cambiartitulo(self):
        cadena = ""
        if self.seleccion1.get() == 1:
            cadena+="Chrome - "
        if self.seleccion2.get() ==1:
            cadena+="FireFox - "
        if self.seleccion3.get() == 1:
            cadena+="Edge - "
        if self.seleccion4.get() ==1:
            cadena+="Opera - "
        self.ventana.title(cadena)
nose = Aplicacion()











