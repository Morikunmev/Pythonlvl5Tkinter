import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        menubar1 = tk.Menu(self.ventana)
        self.ventana.config(menu=menubar1)
        opciones1 = tk.Menu(menubar1)
        opciones1.add_command(label="Rojo",command=self.fijarrojo)
        opciones1.add_command(label="Verde", command=self.fijarverde)
        opciones1.add_command(label="Azul", command=self.fijarazul)
        menubar1.add_cascade(label="Colores",menu=opciones1)

        opciones2 = tk.Menu(menubar1)
        opciones2.add_command(label="640x480",command=self.ventanachica)
        opciones2.add_command(label="1024x800",command=self.ventanagrande)
        menubar1.add_cascade(label="Tamaños",menu=opciones2)
        self.ventana.mainloop()
    def fijarrojo(self):
        self.ventana.configure(background="red")
    def fijarverde(self):
        self.ventana.configure(background="green")
    def fijarazul(self):
        self.ventana.configure(background="blue")
    def ventanachica(self):
        self.ventana.geometry("640x480")
    def ventanagrande(self):
        self.ventana.geometry("1024x800")
aplicacion1 =Aplicacion()